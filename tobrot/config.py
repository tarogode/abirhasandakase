from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "1423837215:AAHD2S1EoTkPEtefGwNJwalD1rO-wtPv0JA"
    APP_ID = 1521555
    API_HASH = "fb8d9f2bb37509c00fd9e2eb4b7a0c5b"
    OWNER_ID = 1387682251
    AUTH_CHANNEL = [-342544769]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMCA97PSbVnmQGcDS_JhHXcOw0CySDGxjzZyWjmrgWHDf9A1n-Rmdg4sVnUDxV9Y5_5tAdbhfpW6_xbF1O9ALAeBj1xmKFQtMubDyGfYB_i1LltJA_e_zJawP-peIK4yzoYrZTvdfP02U2PHfqHiV6WmX5RCUPmXOqHlMG4","token_type":"Bearer","refresh_token":"1//0guQVZQz65RjnCgYIARAAGBASNwF-L9IrWy7b2vaAF3Qyh-UjCszb0xVSG83KYCi4X9taiSfr_9EhDO13oqWNTuoVGris4xENImo","expiry":"2020-12-03T13:41:27.382397538Z"}"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
