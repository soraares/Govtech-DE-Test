There are 2 sources of images, 1. from external clients and 2. from an internal web application.
The external clients can send their image files to an endpoint set up in API gateway, which forwards the images to a lambda proxy, which then passes the images to Amazon Managed Streaming for Apache Kafka (MSK).
The internal web application is hosted within the same VPC as the MSK cluster, and can send images directly to the MSK cluster without any proxy.

Once the images make their way to the MSK cluster, the preprocessing code from the company is run, and the the images are then streamed to Kinesis for analytics. This can be replaced by any other dashboard/analytics service as desired.

Finally the processed images are saved in S3, where they will persist for 7 days before expiring.