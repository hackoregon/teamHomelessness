#! /bin/bash

# Tag, Push and Deploy only if it's not a pull request
if [ -z "$TRAVIS_PULL_REQUEST" ] || [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
  # Tag, Push and Deploy only if we're on the master branch
  if [ "$TRAVIS_BRANCH" == "master" ]; then
    export PATH=$PATH:$HOME/.local/bin
    echo Getting the ECR login...
    eval $(aws ecr get-login --region $AWS_DEFAULT_REGION --no-include-email)
    echo Running docker push command...
    docker push "$DOCKER_REPO"/"$DEPLOY_TARGET"/"$DOCKER_IMAGE":latest
    echo Running ecs-deploy.sh script...
    ./$PROJ_SETTINGS_DIR/bin/ecs-deploy.sh  \
     --service-name "$ECS_SERVICE_NAME" \
     --cluster "$ECS_CLUSTER"   \
     --image "$DOCKER_REPO"/"$DEPLOY_TARGET"/"$DOCKER_IMAGE":latest \
     --timeout 300
   else
     echo "Skipping deploy because branch is not master"
  fi
else
  echo "Skipping deploy because it's a pull request"
fi
