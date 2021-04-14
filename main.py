import DB_Connection
import ArgParse
import xlsx


def say_hello():

    # result process

    # excel 객체 초기화
    excel = xlsx.Xlsx()

    # 실행 개수 제어 db 부하 방지
    LIMIT_COUNT = 10
    curr_count = 0

    # 반복을 위한 for 문
    while True:
        # 실행 개수 제어
        if curr_count == LIMIT_COUNT:
            return

        # xlsx 읽기
        read_param = excel.read_xlsx()

        print(read_param)

        # 종료 조건 다음행 No가 없을 때
        if read_param['eof'] :
            return

        # 가져온 Query 검색용 name 확인
        if read_param['obj_name'] is not None :
            # query 결과 획득
            query = DB_Connection.sql_select(read_param['obj_name'])

            if query is not None :
                # Parse
                aa = ArgParse.conver_args(query)

                # Parse result write
                excel.write_xlsx(read_param, aa)
                # Complete flag write

        curr_count += 1




if __name__ == '__main__':
    # read param
    say_hello()
