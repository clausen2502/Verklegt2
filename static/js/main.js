/* Location Filter JavaScript ---------------------------------------------------------------------- */
function toggleLocationDropdown() {
  toggleDropdown('locationDropdown');
}

/* Type Filter JavaScript -------------------------------------------------------------------------- */
function toggleTypeDropdown() {
  toggleDropdown('typeDropdown');
}

/* Size Filter JavaScript -------------------------------------------------------------------------- */
function toggleSizeDropdown() {
  toggleDropdown('sizeDropdown');
}

/* Room Filter JavaScript -------------------------------------------------------------------------- */
function toggleRoomDropdown() {
  toggleDropdown('roomDropdown');
}

/* Price Filter JavaScript -------------------------------------------------------------------------- */
function togglePriceDropdown() {
  toggleDropdown('priceDropdown');
}

/* General Dropdown Toggle Function ---------------------------------------------------------------- */
function toggleDropdown(id) {
  const dropdown = document.getElementById(id);
  if (!dropdown) return;
  dropdown.style.display = (dropdown.style.display === 'none' || dropdown.style.display === '') ? 'block' : 'none';
}

/* Gallery Toggle JavaScript ----------------------------------------------------------------------- */
function toggleGallerySection() {
  const section = document.getElementById('extra-gallery');
  const galleryButtonText = document.querySelector('#showGalleryButton p');

  if (!section || !galleryButtonText) return;

  const isHidden = section.style.display === 'none' || section.style.display === '';
  section.style.display = isHidden ? 'flex' : 'none';
  galleryButtonText.textContent = isHidden ? 'Hide Gallery' : '30 MYNDIR';
}

/* Show Gallery  ----------------------------------------------------------------------- */
document.addEventListener('DOMContentLoaded', function () {
  const galleryButton = document.getElementById('showGalleryButton');
  if (galleryButton) {
    galleryButton.addEventListener('click', toggleGallerySection);
  }
});

/* Show Custom Type  ----------------------------------------------------------------------- */
document.addEventListener('DOMContentLoaded', function () {
  const typeField = document.querySelector('#id_type');
  const customTypeWrapper = document.querySelector('#custom-type-wrapper');
  if (!typeField || !customTypeWrapper) return;

  const toggleCustomType = () => {
    customTypeWrapper.style.display = typeField.value === 'other' ? 'block' : 'none';
  };

  toggleCustomType();
  typeField.addEventListener('change', toggleCustomType);
});

/* Show Delete Offer Modal  ----------------------------------------------------------------------- */
document.addEventListener('DOMContentLoaded', function () {
  const deleteModal = document.getElementById('globalDeleteOfferModal');
  if (!deleteModal) return;

  deleteModal.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget;
    if (!button) return;

    const offerId = button.getAttribute('data-offer-id');
    const propertyName = button.getAttribute('data-property-name');
    const urlTemplate = button.getAttribute('data-url-template');

    const nameHolder = document.getElementById('propertyNamePlaceholder');
    const form = document.getElementById('deleteOfferForm');
    if (nameHolder && form) {
      nameHolder.textContent = propertyName;
      form.action = urlTemplate.replace('0', offerId);
    }
  });
});

/* Show Delete Property Modal and Gallery Navigation ---------------------------------------------- */
document.addEventListener('DOMContentLoaded', function () {
  const galleryData = document.getElementById('gallery-photos');
  if (!galleryData) return;

  let photos;
  try {
    photos = JSON.parse(galleryData.textContent);
  } catch (e) {
    console.warn('Invalid gallery data');
    return;
  }
  if (!photos || photos.length === 0) return;

  let currentImageIndex = 0;

  const mainImage = document.getElementById('mainImage');
  const prevBtn = document.getElementById('prevMainImageBtn');
  const nextBtn = document.getElementById('nextMainImageBtn');
  if (!mainImage || !prevBtn || !nextBtn) return;

  const updateMainImage = () => {
    mainImage.src = photos[currentImageIndex].image;
  };

  prevBtn.addEventListener('click', () => {
    currentImageIndex = (currentImageIndex - 1 + photos.length) % photos.length;
    updateMainImage();
  });

  nextBtn.addEventListener('click', () => {
    currentImageIndex = (currentImageIndex + 1) % photos.length;
    updateMainImage();
  });

  document.querySelectorAll('.property-sidebar-thumb img').forEach((thumb, index) => {
    thumb.addEventListener('click', () => {
      currentImageIndex = (index + 1) % photos.length;
      updateMainImage();
    });
  });
});

/* Mortgage Calculator ------------------------------------------------------------------- */
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("loan-form");
  if (!form) return;

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const amount = parseFloat(document.getElementById("loan-amount").value);
    const years = parseFloat(document.getElementById("loan-years").value);
    const interest = parseFloat(document.getElementById("loan-interest").value) / 100;

    const months = years * 12;
    const monthlyRate = interest / 12;

    const monthly = (amount * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -months));
    const total = monthly * months;

    document.getElementById("monthly-payment").innerText = monthly.toLocaleString();
    document.getElementById("total-payment").innerText = total.toLocaleString();
    document.getElementById("loan-results").classList.remove("d-none");
  });
});

/* Cookie Banner ------------------------------------------------------------------------ */
document.addEventListener('DOMContentLoaded', function () {
  const banner = document.getElementById('cookie-banner');
  const acceptBtn = document.getElementById('cookie-accept');
  const declineBtn = document.getElementById('cookie-decline');

  if (!banner || !acceptBtn || !declineBtn) return;

  const hasConsented = localStorage.getItem('cookieConsent');

  // Show or hide banner
  if (!hasConsented) {
    console.log("No prior cookie choice — showing banner");
    banner.style.cssText = 'display: flex !important';
  } else {
    console.log("Consent already handled — hiding banner");
    banner.style.display = 'none';
  }

  // Accept
  acceptBtn.addEventListener('click', () => {
    localStorage.setItem('cookieConsent', 'accepted');
    banner.style.display = 'none';
    console.log("Consent accepted");
  });

  // Decline
  declineBtn.addEventListener('click', () => {
    localStorage.setItem('cookieConsent', 'declined');
    banner.style.display = 'none';
    console.log("Consent declined");
  });
});


/* Sort-by dropdown triggers form submit ------------------------------------------------ */
document.addEventListener("DOMContentLoaded", function () {
  const sortSelect = document.getElementById("sortSelect");
  const filterForm = document.getElementById("filterForm");

  if (sortSelect && filterForm) {
    sortSelect.addEventListener("change", () => filterForm.submit());
  }
});
