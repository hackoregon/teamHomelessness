#! /bin/bash
# Setup Project Specfics - No Secrets
export ECS_CLUSTER=
export ECS_PROJECT=
export ECS_PORT=8000
export ECS_CLUSTER_SIZE=
export ECS_INSTANCE_TYPE=
export AWS_REGION=
export AWS_KEY_PAIR=
export DOCKER_REPO=hackoregon
export DOCKER_WEB_IMAGE=homeless-api
echo "##############################"
echo  Your Environement
echo "##############################"
echo ECS_CLUSTER: $ECS_CLUSTER
echo ECS_PROJECT: $ECS_PROJECT
echo ECS_PORT: $ECS_PORT
echo ECS_CLUSTER_SIZE: $ECS_CLUSTER_SIZE
echo ECS_INSTANCE_TYPE: $ECS_INSTANCE_TYPE
echo AWS_REGION: $AWS_REGION
echo AWS_KEY_PAIR: $AWS_KEY_PAIR
echo DOCKER_REPO: $DOCKER_REPO
echo DOCKER_WEB_IMAGE: $DOCKER_WEB_IMAGE
