from preprocessor.models import VideoData
from django.http import HttpResponse
import os
import glob
import boto3
from config.settings import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,AWS_STORAGE_BUCKET_NAME

s3 = boto3.resource(
        's3',
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
)
bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)

path = "https://aws-s3-capstone.s3.ap-northeast-2.amazonaws.com/clippingVideo/"


def db_delete(delete_list):
    for data in delete_list:
        print(data)
        queryset = VideoData.objects.all()
        queryset = queryset.filter(videoId=data.get('videoId'),
                                   keyword=data.get('keyword'),
                                   model_tag=data.get('model_tag'),
                                   startTime=data.get('startTime'),
                                   endTime=data.get('endTime'),
                                   video_number=data.get('video_number'),
                                   )
        queryset.delete()
        print("delete_complete!!!")

    return HttpResponse("delete_db!!")


def data_delete(delete_list):
    location = "/Users/zigje9/Desktop/jenesis/public/frames/"
    os.chdir(location)
    for data in delete_list:
        os.remove('%s_%s_%d-%d_%d.mp4' % (data.get('model_tag'),
                                          data.get('videoId'),
                                          data.get('startTime'),
                                          data.get('endTime'),
                                          data.get('video_number'),
                                         )
                 )
        '''
         
        후에 s3 에 있는 전처리 완료된 영상을 삭제
        
        '''

    return HttpResponse("delete_data!!!")



# 'C:/Users/jaehee/capstone/Material_Ui_Capstone/publi c/clippingVideo/'
# 'C:/Users/jaehee/capstone/Material_Ui_Capstone/public/thumbnails/'

# '/Users/zigje9/Desktop/jenesis/public/clippingVideo/'
# '/Users/zigje9/Desktop/jenesis/public/thumbnails/'

# 'C:/Users/LG/Desktop/Material_Ui_Capstone/public/clippingVideo/'
# 'C:/Users/LG/Desktop/Material_Ui_Capstone/public/thumbnails/'