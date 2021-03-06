FROM amazon/aws-glue-libs:glue_libs_1.0.0_image_01 
COPY . /home/glue-test
RUN find / -name "aws-glue-libs"
WORKDIR /home/glue-test/
ENTRYPOINT ["/home/aws-glue-libs/bin/gluepytest"]


#CMD /home/spark-2.4.3-bin-spark-2.4.3-bin-hadoop2.8/bin/spark-submit job-test.py
# # FROM amazon/aws-glue-libs:glue_libs_1.0.0_image_01 
# # COPY . /home/jupyter/glue-job
# # CMD ["/home/spark-2.4.3-bin-spark-2.4.3-bin-hadoop2.8/bin/spark-submit", "/home/jupyter/glue-job/job-test.py"]

# FROM python:3.7-buster
# WORKDIR /home
# RUN apt update
# RUN pip install pytest
# RUN pip install pandas
# #RUN python --version
# RUN apt install -y wget gnupg software-properties-common
# RUN wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | apt-key add 
# RUN add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/
# RUN apt update -y
# RUN apt install adoptopenjdk-8-hotspot -y
# RUN apt-get -y install git
# RUN git clone https://github.com/awslabs/aws-glue-libs.git
# RUN apt-get install wget
# RUN wget https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-common/apache-maven-3.6.0-bin.tar.gz && tar xvf apache-maven-3.6.0-bin.tar.gz
# RUN wget https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-3.0/spark-3.1.1-amzn-0-bin-3.2.1-amzn-3.tgz &&  tar xvf spark-3.1.1-amzn-0-bin-3.2.1-amzn-3.tgz
# RUN export MAVEN=/root/apache-maven-3.6.0-bin
# RUN export PATH=$PATH:$MAVEN/bin
# RUN export SPARK_HOME=/root/spark-3.1.1-amzn-0-bin-3.2.1-amzn-3
# RUN export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
# RUN export PYSPARK_PYTHON=$(which python)
# RUN pip install awsglue-local
# #RUN pip install py4j
# RUN pip install boto3
# #RUN git clone https://github.com/Tarini-27/glue-job-test
# WORKDIR glue-job-test
# RUN pwd
# RUN find / -name "aws-glue-libs"
# ENTRYPOINT ["/home/aws-glue-libs/bin/gluepytest"]
# #COPY . /home
# #RUN ls
# #WORKDIR "home/"
# #RUN pwd
# #ENTRYPOINT ["python3", "test.py"]
