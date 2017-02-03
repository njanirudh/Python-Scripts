import boto3

#returns a list of all buckets
def getBucketNameList():

    bucketList =[]
    response = s3client.list_buckets()

    for bucket in response["Buckets"]:
        bucketList.append(bucket['Name'])

    return bucketList

#------------------------------------------------------

def getItemsInBucket(bucket_name):
    bucket_obj_list = []
    for key in s3client.list_objects(Bucket=bucket_name)['Contents']:
        #print(" - " + key['Key'])
        bucket_obj_list.append(key['Key'])

    return bucket_obj_list

#------------------------------------------------------
def upLoadFile(file_path , bucket_name , key):
    #Upload to a given bucket
    s3client.upload_file(file_path, bucket_name, key)
    print "Successfully uploaded the file to S3"

#------------------------------------------------------

# *** Give file name for the downloaded file with the apt format eg '.jpg' , '.png' etc
def downloadFile(bucket_name ,key , file_name):
    #Download a file
    s3_response = s3client.get_object(Bucket = bucket_name,Key = key)
    #print(s3_response)

    print "Successfully downloaded the file from S3"

    # Save the file to an image
    #The response is a stream-body
    img_stream =s3_response['Body'].read()
    imgFile = open(file_name,"wb")
    imgFile.write(img_stream)

#------------------------------------------------------

def deleteFile(bucket_name , key):
    s3_del_response = s3client.delete_object(Bucket = bucket_name , Key = key)

    #print s3_del_response['DeleteMarker']



if __name__ == '__main__':
    # Create a boto client (Requires Aws configuration file)
    s3client = boto3.client('s3')

    # Lists and Prints bucket names
    bucket_list = getBucketNameList()

    for bucket in bucket_list:
        print bucket

    #List and Prints items in a bucket
    bucket_items = getItemsInBucket(bucket_list[0])

    for items in bucket_items :
        print " - " + items

    downloadFile(bucket_list[0] , "pipe_type_01/IMG_2142.JPG" , "IMG_2154.JPG")

    deleteFile("cm-s3-test-01","tmp.txt")




