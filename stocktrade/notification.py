import sys
import yaml
import requests

def main():
    send_line_notify('てすとてすと')

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    try:
        with open(".conf/personal_info.yaml") as file:
            config = yaml.safe_load(file)
            line_notify_token = config["LINE"]["API_Token"]
            line_notify_api = 'https://notify-api.line.me/api/notify'
            headers = {'Authorization': f'Bearer {line_notify_token}'}
            data = {'message': f'message: {notification_message}'}
            requests.post(line_notify_api, headers = headers, data = data)
    except Exception as e:
        print('Exception occurred while loading YAML...', file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)
    
if __name__ == "__main__":
    main()