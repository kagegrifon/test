async function loadRepos() {
  const response = await fetch("/api/repos");
  const repos = await response.json();
  render(repos);
}

function render(repos) {
  const list = document.querySelector("#repo-list");
  list.textContent = "";

  repos.forEach((repo) => {
    const card = document.createElement("article");
    card.className = "repo-card";
    card.innerHTML =
      '<h2 class="name"></h2>' +
      '<p class="desc"></p>' +
      '<p class="meta"><span class="lang"></span> · <span class="updated"></span></p>';

    card.querySelector(".name").textContent = repo.name;
    card.querySelector(".lang").textContent = repo.language;
    card.querySelector(".updated").textContent = repo.updated_at;

    // TODO: небезопасный вывод
    card.querySelector(".desc").innerHTML = repo.description;

    list.appendChild(card);
  });
}

loadRepos();
