// document.getElementById('studentLogin').addEventListener('click', function() {
//   alert('Redirecting to Student Login Page...');
//   // window.location.href = 'student-login.html';
// });

// document.getElementById('adminLogin').addEventListener('click', function() {
//   alert('Redirecting to Admin Login Page...');
//   // window.location.href = 'admin-login.html';
// });


// =========================
// script.js
// =========================

// Handle Lost or Found Form Submission
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("itemForm");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();

      const itemName = form.querySelector('input[placeholder="e.g., iPhone 13 Pro"]').value;
      const category = form.querySelector("select").value;
      const desc = form.querySelector("textarea").value;
      const date = form.querySelector('input[type="date"]').value;
      const location = form.querySelector('input[placeholder*="Library"]').value;

      // Check if this page is lost or found
      const status = document.title.includes("Lost") ? "LOST" : "FOUND";

      // Image Upload (optional)
      const fileInput = form.querySelector("#upload");
      let imageSrc = "dummy.jpg"; // default image
      if (fileInput && fileInput.files[0]) {
        imageSrc = URL.createObjectURL(fileInput.files[0]);
      }

      // Make item object
      const itemData = {
        name: itemName,
        category,
        desc,
        date,
        location,
        status,
        imageSrc,
      };

      // Get old items from localStorage
      const existing = JSON.parse(localStorage.getItem("items")) || [];
      existing.push(itemData);

      // Save back to localStorage
      localStorage.setItem("items", JSON.stringify(existing));

      alert(`Your ${status.toLowerCase()} item has been submitted!`);
      form.reset();
    });
  }

  // ======================
  // Display items on Search Page
  // ======================
  if (document.title.includes("Item Listings")) {
    const container = document.querySelector(".card-container");
    const items = JSON.parse(localStorage.getItem("items")) || [];

    items.forEach((item) => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
        <div class="photo">
          <img src="${item.imageSrc}" alt="${item.name}">
        </div>
        <h3>${item.name} <span class="status ${item.status.toLowerCase()}">${item.status}</span></h3>
        <p class="category">${item.category}</p>
        <p class="desc">${item.desc}</p>
        <p class="info">📍 ${item.location}</p>
        <p class="info">📅 ${item.date}</p>
        <button><a href="detail-card.html">View Details</a></button>
      `;
      container.appendChild(card);
    });
  }
});


document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault();
  alert("Login successful (demo only)");
});



// lost file ka js 

// Select elements
const uploadInput = document.getElementById("upload");
const uploadLabel = document.querySelector(".upload-label");

// When file is selected
uploadInput.addEventListener("change", function () {
  const file = this.files[0];
  if (file) {
    const reader = new FileReader();

    reader.addEventListener("load", function () {
      uploadLabel.innerHTML = `
        <img src="${this.result}" alt="Uploaded Image" class="preview-img" />
        <p class="upload-text">${file.name}</p>
      `;
    });

    reader.readAsDataURL(file);
  }
});



// ====detail- view of card ====



