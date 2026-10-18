// Get elements
const statusElement = document.getElementById("itemStatus");
const actionContainer = document.getElementById("actionContainer");

// Get the actual status (trim spaces & uppercase)
const statusText = statusElement.textContent.trim().toUpperCase();

// Logic: If LOST → Show message instead of button
if (statusText === "LOST") {
  actionContainer.innerHTML = `
    <div class="lost-msg">
      This is a lost item. If you found something similar, please report it using 
      the <strong>"Report Found Item"</strong> feature.
    </div>
  `;
} 
// Else show button normally
else if (statusText === "FOUND") {
  actionContainer.innerHTML = `
    <button class="claim-btn"><a href="claim-item.html">Claim Item</a></button>
  `;
}
