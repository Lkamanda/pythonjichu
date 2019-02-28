'''
data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
前10秒查询，后十秒预定
查询
locationId 2-8
date   2019-01-30
roomType  video(1/4) normal,

预定
boardroomId  range(1,10)
date  2019-01-21
startTime 08:00 - 20:00  / x = 8 - 20
endTime

@RequestParam(value = "boardroomId") Long boardroomId,
@RequestParam(value = "userName") String userName,
@RequestParam(value = "bookerName") String bookerName,
@RequestParam(value = "date") String date,
@RequestParam(value = "startTime") String startTime,
@RequestParam(value = "endTime") String endTime,
@RequestParam(value = "timestamp") Long timestamp,
@RequestParam(value = "code") String code
'''
import pandas
import time
import random
import datetime
# 查询
def generate_data():
    generate_data = []
    for i in range(0, 3000):
        #max_date = datetime.date.today() + datetime.timedelta(days=7)
        max_date = '2019-2-7'
        roomType_list = ['video', 'normal', 'normal', 'normal']
        roomType = random.choice(roomType_list)
        localtionId_list = [i for i in range(1, 10)]
        localtionId = random.choice(localtionId_list)
        meeting_date = {
            "date": max_date,
            "roomType": roomType,
            "localtionId": localtionId,
        }
        generate_data.append(meeting_date)

    return generate_data

# 预定
def meeting_reserve():
    reserve_data = []
    for n in range(0, 3000):
        boardroomId_list = [i for i in range(1, 10)]
        boardroomId = random.choice(boardroomId_list)

        data = datetime.date.today() + datetime.timedelta(days=7)
        #data = '2019-2-7'
        print(type(data))
        start_list = [i for i in range(8, 20)]
        for y in range(0, 3):
            for x in [10, 11, 13, 14, 15, 16, 17]:
                    start_list.append(x)
        z = random.choice(start_list)
        starttime = '{}:00'.format(z)
        endtime = '{}:00'.format(z+1)
        username_list = [m for m in range(1, 11)]
        userName = random.choice(username_list)
        print(userName)
        bookname = "1"
        timestamp = 1
        code = "code"
        reserve_dict = {
            "code": code,
            "timestamp": timestamp,
            "userName": userName,
            "bookname": bookname,
            "boardroomId": boardroomId,
            "date": data,
            "endTime": endtime,
            "startTime": starttime
        }
        reserve_data.append(reserve_dict)
    return reserve_data


def chaxu():
    data = generate_data()
    pd = pandas.DataFrame(data)
    pd.to_csv('会议查询数据.csv')

def yuding():
    data = meeting_reserve()
    pd = pandas.DataFrame(data)
    pd.to_csv('会议预定数据.csv')


if __name__ == '__main__':
    chaxu()
    yuding()

