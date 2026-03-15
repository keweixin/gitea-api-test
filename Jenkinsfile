pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'gitea/gitea:1.25'
        MYSQL_IMAGE = 'mysql:8.0'
        GITEA_CONTAINER = 'gitea'
        MYSQL_CONTAINER = 'jenkins-gitea-mysql'
        BASE_URL = 'http://127.0.0.1:3000/api/v1'
        USERNAME = 'admin_user'
        PASSWORD = 'Admin123456'
        OWNER = 'admin_user'
        PUBLIC_USER = 'admin_user'
        REPO_NAME_BASE = 'repo-demo-public'
        REPO_NAME_TEMP = 'repo-demo-temp'
        PRIVATE_REPO_NAME = 'repo-demo-private'
        COLLABORATOR = 'admin_user'
        MYSQL_HOST = '127.0.0.1'
        MYSQL_PORT = '3308'
        MYSQL_USER = 'gitea'
        MYSQL_PASSWORD = 'gitea_secure_password'
        MYSQL_DB = 'gitea'
        TOKEN = credentials('gitea-token')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    sh '''
                        # Stop existing containers if any
                        docker rm -f ${GITEA_CONTAINER} ${MYSQL_CONTAINER} 2>/dev/null || true
                    '''
                }
            }
        }

        stage('Start Dependencies') {
            steps {
                script {
                    // Start MySQL
                    sh """
                        docker run -d --name ${MYSQL_CONTAINER} \
                            -e MYSQL_ROOT_PASSWORD=root_secure_password \
                            -e MYSQL_DATABASE=gitea \
                            -e MYSQL_USER=gitea \
                            -e MYSQL_PASSWORD=gitea_secure_password \
                            -p 3308:3306 \
                            ${MYSQL_IMAGE}
                    """

                    // Wait for MySQL to be ready
                    sh 'sleep 30'

                    // Start Gitea
                    sh """
                        docker run -d --name ${GITEA_CONTAINER} \
                            --link ${MYSQL_CONTAINER}:db \
                            -e USER_UID=1000 \
                            -e USER_GID=1000 \
                            -e GITEA__security__INSTALL_LOCK=true \
                            -e GITEA__service__DISABLE_REGISTRATION=true \
                            -e GITEA__database__DB_TYPE=mysql \
                            -e GITEA__database__HOST=db:3306 \
                            -e GITEA__database__NAME=gitea \
                            -e GITEA__database__USER=gitea \
                            -e GITEA__database__PASSWD=gitea_secure_password \
                            -e GITEA__server__ROOT_URL=http://127.0.0.1:3000/ \
                            -p 3000:3000 \
                            -p 2222:22 \
                            ${DOCKER_IMAGE}
                    """
                }
            }
        }

        stage('Wait for Gitea') {
            steps {
                script {
                    echo 'Waiting for Gitea to be ready...'
                    sh '''
                        for i in {1..60}; do
                            if curl -fsS http://127.0.0.1:3000/ >/dev/null 2>&1; then
                                echo "Gitea is ready!"
                                exit 0
                            fi
                            echo "Waiting... ($i/60)"
                            sleep 5
                        done
                        echo "Gitea failed to start"
                        exit 1
                    '''
                }
            }
        }

        stage('Bootstrap Test Data') {
            steps {
                script {
                    sh """
                        # Create admin user
                        docker exec ${GITEA_CONTAINER} gitea admin user create \
                            --username admin_user \
                            --password Admin123456 \
                            --email admin@test.com \
                            --admin \
                            --must-change-password=false || true

                        # Wait for user creation
                        sleep 5

                        if [ -z "\${TOKEN}" ]; then
                            echo "Missing Jenkins credential: gitea-token"
                            exit 1
                        fi

                        # Create test repository
                        STATUS=\$(curl -sS -o /tmp/repo.json -w "%{http_code}" \
                            -X POST \
                            -H "Authorization: token \${TOKEN}" \
                            -H "Content-Type: application/json" \
                            -d '{"name":"repo-demo-public","description":"created by jenkins","private":false}' \
                            http://127.0.0.1:3000/api/v1/user/repos)

                        if [ "\${STATUS}" != "201" ] && [ "\${STATUS}" != "200" ] && [ "\${STATUS}" != "409" ]; then
                            echo "Failed to create base repository, status=\${STATUS}"
                            cat /tmp/repo.json
                            exit 1
                        fi
                    """
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p reports allure-results
                    pytest -v \
                        --html=reports/pytest-report.html \
                        --self-contained-html \
                        --alluredir=allure-results \
                        -m "not db"
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    sh '''
                        if command -v allure &> /dev/null; then
                            allure generate allure-results -o allure-report --clean || true
                        else
                            echo "Allure not installed, skipping report generation"
                        fi
                    '''
                }
            }
        }

        stage('Publish Reports') {
            steps {
                script {
                    // Publish HTML report
                    publishHTML(target: [
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'pytest-report.html',
                        reportName: 'Pytest Report'
                    ])

                    // Archive test results
                    junit allowEmptyResults: true, testResults: 'allure-results/*.xml'
                }
            }
        }
    }

    post {
        always {
            script {
                // Cleanup containers
                sh '''
                    docker rm -f ${GITEA_CONTAINER} ${MYSQL_CONTAINER} 2>/dev/null || true
                '''
            }

            // Archive artifacts
            archiveArtifacts artifacts: 'reports/**,allure-results/**', allowEmptyArchive: true
        }

        failure {
            // Show logs on failure
            sh '''
                docker logs ${GITEA_CONTAINER} || true
                docker logs ${MYSQL_CONTAINER} || true
            '''
        }
    }
}
