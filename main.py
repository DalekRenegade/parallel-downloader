from Downloader import *

url_metadata = "https://os.unil.cloud.switch.ch/fma/fma_metadata.zip"
url_small = "https://os.unil.cloud.switch.ch/fma/fma_small.zip"
url_medium= "https://os.unil.cloud.switch.ch/fma/fma_medium.zip"
url_large = "https://os.unil.cloud.switch.ch/fma/fma_large.zip"
url_full = "https://os.unil.cloud.switch.ch/fma/fma_full.zip"

sha1sum_metadata = 'f0df49ffe5f2a6008d7dc83c6915b31835dfe733'
sha1sum_small = 'ade154f733639d52e35e32f5593efe5be76c6d70'
sha1sum_medium = 'c67b69ea232021025fca9231fc1c7c1a063ab50b'
sha1sum_large = '497109f4dd721066b5ce5e5f250ec604dc78939e'
sha1sum_full = '0f0ace23fbe9ba30ecb7e95f763e435ea802b8ab'

threads = 10

obj = Downloader(url=url_large, number_of_threads=threads, destination_directory='D:\\audio-mashup-dataset',
                 source_sha1sum=sha1sum_large)

obj.start_download()
# obj.merge_chunks()
print(obj.get_metadata())
print(obj.get_remote_crc32c())
print(obj.get_downloaded_crc32c_large())
print(obj.get_downloaded_sha1_large())
