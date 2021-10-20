# FROM amazon/aws-glue-libs:glue_libs_1.0.0_image_01 
# COPY . /home/jupyter/glue-job
# CMD ["/home/spark-2.4.3-bin-spark-2.4.3-bin-hadoop2.8/bin/spark-submit", "/home/jupyter/glue-job/job-test.py"]

FROM ubuntu:18.04
RUN apt-get update && apt -y install python3-pip
RUN pip3 install pytest
RUn pip3 install pandas
RUN apt -y install openjdk-8-jdk-headless
RUN apt-get -y install git
RUN git clone https://github.com/awslabs/aws-glue-libs.git
RUN apt-get install wget
RUN wget https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-common/apache-maven-3.6.0-bin.tar.gz && tar xvf apache-maven-3.6.0-bin.tar.gz
RUN wget https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-3.0/spark-3.1.1-amzn-0-bin-3.2.1-amzn-3.tgz &&  tar xvf spark-3.1.1-amzn-0-bin-3.2.1-amzn-3.tgz
RUN export MAVEN=/root/apache-maven-3.6.0-bin
RUN export PATH=$PATH:$MAVEN/bin
RUN export SPARK_HOME=/root/spark-3.1.1-amzn-0-bin-3.2.1-amzn-3
RUN export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
RUN export PYSPARK_PYTHON=$(which python)
RUN pip3 install pyspark
RUN pip3 install py4j
RUN git clone https://github.com/Tarini-27/glue-job-test
WORKDIR "/home/glue-job-test"
RUN ../home/aws-glue-libs/bin/gluepytest test_spark.py
#COPY . /home
#RUN ls
#WORKDIR "home/"
#RUN pwd
#ENTRYPOINT ["python3", "test.py"]

