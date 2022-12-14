if not exist "openapi-generator-cli-6.2.1.jar" (
    curl -o "openapi-generator-cli-6.2.1.jar" https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.2.1/openapi-generator-cli-6.2.1.jar
)

py main.py --docs

java -jar .\openapi-generator-cli-6.2.1.jar generate -i .\openapi.json -g javascript -o ../frontend/src/crowdlabel-api