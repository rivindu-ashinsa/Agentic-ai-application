import requests, os
from dotenv import load_dotenv

load_dotenv()

def fetch_repo_code(repo_url):
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"}
    owner, repo = repo_url.rstrip("/").split("/")[-2:]

    def get_files(path=""):
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(f"Error fetching {url}: {r.status_code}")
            return []
        data = r.json()
        files = []
        for item in data:
            if item["type"] == "file":
                if item.get("size", 0) < 200_000:
                    try:
                        file_text = requests.get(item["download_url"], headers=headers).text
                        files.append({"path": item["path"], "content": file_text})
                    except Exception as e:
                        print(f"Error reading {item['path']}: {e}")
            elif item["type"] == "dir":
                files.extend(get_files(item["path"]))
        return files

    return get_files()


# files = fetch_repo_code("https://github.com/rivindu-ashinsa/Doc-Drafter")
# print(f"Fetched {len(files)} files.")
# print(type(files))
# print("Example:", type(files[2]))
