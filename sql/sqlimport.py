import os
import time
import pymysql.cursors

connection = pymysql.connect(host = "localhost", user = 'rigi', password = 'pwd@rigi', db = 'events_db', local_infile = True)

def loadMultData(cursor, file):
	load = '''LOAD DATA LOCAL INFILE %s INTO TABLE events_data
				FIELDS TERMINATED BY ','
				LINES TERMINATED BY '\n'
				IGNORE 1 ROWS (USERID, PRIMARY_FINGERPRINT, USER_BROWSER, USER_BROWSER_VERSION, USER_OS, USER_OS_VERSION, USER_HOSTADDRESS, SESSIONID, ORIGINAL_VIDEO_CONTENT_ID, VIDEO_CONTENT_ID, VIDEO_CONTENT_TITLE, ORIGINAL_VIDEO_CATEGORY_ID, VIDEO_CATEGORY_ID, VIDEO_CATEGORY_TITLE, VIDEO_TYPE, VIDEO_DURATION, SESSION_STARTDT, SESSION_ENDDT, CLICK_COUNT, ADPLAY_COUNT, PLAY_COUNT, PAUSE_COUNT, RESUME_COUNT, AB_FLAG, SEEK_COUNT, BUFFER_COUNT, TOTAL_BUFFER_TIME, MAX_BUFFER_TIME, USR_TOT_WATCHING_DUR, USR_ACT_TOT_WATCHING_DUR, ISP_PROVIDER, ISMOBILE, MOBILE_DEVICE, ISP_TAG, MOBILETYPE, APP_TAG, THREE_G_TAG, CONTENT_TYPE, IPCOUNTRY, SUBDIVISION_1, SUBDIVISION_2, IPCITY, APP_VERSION)
            '''
	cursor.execute(load, (file))
	connection.commit()
	print('Added rows: ', cursor.rowcount)
	print("Successfully imported file {}".format(file))


def main(data_dir, cursor):
    s = time.time()
    for f in sorted(os.listdir(data_dir)):
        if f.endswith(".csv"):
            file = os.path.join(data_dir, f)
            loadMultData(cursor, file)
    e = time.time()
    total_time = time.strftime("%H:%M:%S", time.gmtime(e-s))
    print("Finish importing {} in {}".format(data_dir, total_time))

if __name__ == '__main__':
    cursor = connection.cursor()
    # loadMultData(cursor, "../try.csv")
    #main("../../events/sql/december", cursor)
    # main("../../events/sql/january", cursor)
    # main("../../events/sql/february", cursor)
    main("../../events/sql/march", cursor)
    main("../../events/sql/april", cursor)
    main("../../events/sql/may", cursor)
    cursor.close()