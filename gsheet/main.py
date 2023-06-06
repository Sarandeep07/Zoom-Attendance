from http import client
import gspread
import pandas


def authorize():
    gc = gspread.service_account(filename='credentials.json')
    client = gspread.authorize(gc)


def get_data():
    spreadsheet = client.open("Zoom Links")
    df = pandas.DataFrame(spreadsheet.get_worksheet(0).get_all_records())
    print(df)


def get_meet_links(df):
    meet_links = df['Meet Links']
    return meet_links


def get_meeting_id(url):
    return url.split('/')[-1]


if __name__ == '__main__':
    authorize()
    get_data()
    get_meet_links()
    get_meeting_id()
