import subprocess
import platform


def ping_websites(websites, count=3):
    if platform.system() == 'Windows':
        cmd = ['ping', '-n', str(count)]
    else:
        cmd = ['ping', '-c', str(count)]

    for website in websites:
        try:
            result = subprocess.run(cmd + [website],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)
            print(f"Pinging {website}...")
            print(result.stdout)
        except Exception as e:
            print(f"Error pinging {website}: {str(e)}")


sites_for_checking = ['www.ringcentral.com', 'www.youtube.com']
ping_websites(sites_for_checking)
