import json
import os

from flask import Flask, Response, send_from_directory

import config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(BASE_DIR, "web")
DATA_FILE = os.path.join(BASE_DIR, "data", "repos.json")

app = Flask(__name__, static_folder=None)


def load_repos():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    return send_from_directory(WEB_DIR, "index.html")


@app.route("/app.js")
def app_js():
    return send_from_directory(WEB_DIR, "app.js")


@app.route("/api/repos")
def api_repos():
    repos = load_repos()
    return Response(
        json.dumps(repos, ensure_ascii=False),
        mimetype="application/json",
    )


@app.route("/stats")
def stats():
    repos = load_repos()
    top = repos[: config.MAX_REPOS]
    languages = {}
    for repo in top:
        languages[repo["language"]] = languages.get(repo["language"], 0) + 1
    rows = "".join(
        "<tr><td>{}</td><td>{}</td></tr>".format(name, count)
        for name, count in sorted(languages.items())
    )
    return (
        "<h1>Статистика</h1>"
        "<p>Всего репозиториев: {}</p>"
        "<table>{}</table>"
        '<p><a href="/">К витрине</a></p>'
    ).format(len(repos), rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(config.PORT), debug=config.DEBUG)
