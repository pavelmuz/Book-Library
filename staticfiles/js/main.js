let searchForm = document.getElementById("searchForm");
let pageLinks = document.getElementsByClassName("page-link");

if (searchForm) {
  for (page of pageLinks) {
    page.addEventListener("click", function (e) {
      e.preventDefault();

      let page = this.dataset.page;

      searchForm.innerHTML += `<input value=${page} name="page" hidden/>`;
      searchForm.submit();
    });
  }
}
