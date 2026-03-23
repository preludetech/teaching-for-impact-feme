(function () {
  const PASSWORD = "training";

  function checkAuth() {
    return sessionStorage.getItem("authenticated") === "true";
  }

  function showLogin() {
    document.body.innerHTML = `
      <div style="
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
        font-family:sans-serif;
      ">
        <div>
          <h2>Enter password</h2>
          <input type="password" id="pw" />
          <button onclick="checkPassword()">Submit</button>
          <p id="error" style="color:red;"></p>
        </div>
      </div>
    `;

    window.checkPassword = function () {
      const input = document.getElementById("pw").value;
      if (input === PASSWORD) {
        sessionStorage.setItem("authenticated", "true");
        location.reload();
      } else {
        document.getElementById("error").innerText = "Incorrect password";
      }
    };
  }

  if (!checkAuth()) {
    document.addEventListener("DOMContentLoaded", showLogin);
  }
})();