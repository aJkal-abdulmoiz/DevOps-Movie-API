pipeline{
	agent any
	environment{
		LOG_LEVEL='INFO'
		RELEASE='20.04'
	}
	stages{
		stage('Build'){
			steps{
				echo "Building release ${RELEASE} with log level ${LOG_LEVEL}..."
			}
		}
		stage('Test')
		{
			steps{
				echo "Testing. I can see release ${RELEASE} with log level ${LOG_LEVEL}."
			}
		}
	}
}
