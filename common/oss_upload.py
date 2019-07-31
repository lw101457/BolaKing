import uuid

import oss2

from fastapi import UploadFile


def upload_image(file: UploadFile):
    file_name = str(uuid.uuid4()) + file.filename.split(".")[-1]
    file = file.file
    accesskeyid = 'LTAIv816izYZhMkl'
    accesskey = 'Psfru0eOBJVFUELx9AsmLVeNsPnCh1'
    endpoint = 'oss-ap-southeast-1.aliyuncs.com'
    bucket_name = 'cashloan-ly'
    auth = oss2.Auth(accesskeyid, accesskey)
    bucket = oss2.Bucket(auth, endpoint=endpoint, bucket_name=bucket_name)
    bucket.put_object(file_name, file.read())
    image_url = '%s://%s.%s/%s' % ('http', bucket_name, endpoint, file_name)
    return {'image': image_url}
