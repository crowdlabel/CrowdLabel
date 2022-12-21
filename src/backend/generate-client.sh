wget --no-clobber https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.2.1/openapi-generator-cli-6.2.1.jar
python3.11 main.py --docs
java -jar openapi-generator-cli-6.2.1.jar generate -i openapi.json -g javascript -o ../frontend/src/crowdlabel-api

cd ../frontend/src
python3.11 patch-api.py