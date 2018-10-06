node {
    stage('Clone repository') {
        checkout scm
    }

    stage('Initialize'){
        def dockerHome = tool 'docker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }

    stage('Build image') {
        sh 'docker build -t gcr.io/lhgames-2018/ai-oye:version-$BUILD_NUMBER .'
    }

    stage('Push image') {
        sh 'docker push gcr.io/lhgames-2018/ai-oye:version-$BUILD_NUMBER'
    }
}
