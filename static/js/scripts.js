let BASE = document.querySelectorAll('.showBase');
function showGas() {
    let gasElements = document.querySelectorAll('.showGaz');
    let fuelElements = document.querySelectorAll('.showFuel');
    
    gasElements.forEach(element => {
        element.style.display = 'block';
        if (element.tagName === 'INPUT') {
            element.value = '';
        }
    });
    BASE.forEach(element => {
        element.classList.remove('showBase');
        element.classList.add('gg')
    });
    
    BASE.forEach(element => {
        element.classList.remove('showBase');
        element.classList.add('gg')

    });
    fuelElements.forEach(element => {
        element.style.display = 'none';
        if (element.tagName === 'INPUT') {
            element.value = '0';
        }
    });
}

function showPetrol() {
    let gasElements = document.querySelectorAll('.showGaz');
    let fuelElements = document.querySelectorAll('.showFuel');
    
    gasElements.forEach(element => {
        element.style.display = 'none';
        if (element.tagName === 'INPUT') {
            element.value = '0';
        }
    });
    BASE.forEach(element => {
        element.classList.remove('showBase');
        element.classList.add('gg')

    });
    
    BASE.forEach(element => {
        element.classList.remove('showBase');
        element.classList.add('gg')

    });
    fuelElements.forEach(element => {
        element.style.display = 'block';
        if (element.tagName === 'INPUT') {
            element.value = '';
        }
    });
}

function showBoth() {
    let gasElements = document.querySelectorAll('.showGaz');
    let fuelElements = document.querySelectorAll('.showFuel');
    
    gasElements.forEach(element => {
        element.style.display = 'none';
        if (element.tagName === 'INPUT') {
            element.value = '0';
        }
    });fuelElements.forEach(element => {
        element.style.display = 'none';
        if (element.tagName === 'INPUT') {
            element.value = '0';
        }
    });
    BASE.forEach(element => {
        element.classList.remove('showBase');
        element.classList.add('gg')

    });
    
    BASE.forEach(element => {
        element.classList.remove('showBase');
        element.classList.add('gg')

    });
    
    
    gasElements.forEach(element => {
        element.style.display = 'block';
        if (element.tagName === 'INPUT') {
            element.value = '';
        }
    });

    fuelElements.forEach(element => {
        element.style.display = 'block';
        if (element.tagName === 'INPUT') {
            element.value = '';
        }
    });
}
document.addEventListener('DOMContentLoaded', () => {
    const pages = document.querySelectorAll('.page');
    let nextButton = document.getElementById('nextButton');
    const prevButton = document.getElementById('prevButton');
    let currentPageIndex = 0;

    // نمایش صفحه اول
    pages[currentPageIndex].classList.add('active');

    // بروزرسانی وضعیت دکمه‌ها
    function updateButtons() {
        prevButton.disabled = currentPageIndex === 0;
        nextButton.disabled = currentPageIndex === pages.length - 1;

        if (currentPageIndex === pages.length - 1) {
            // اگر در صفحه آخر هستیم، دکمه "ادامه" را به "ذخیره" تغییر دهید
            nextButton.innerHTML = "ذخیره";
        } else {
            // در غیر این صورت، دوباره دکمه را به "ادامه" تنظیم کنید
            nextButton.innerHTML = "ادامه";
        }
    }

    // بروزرسانی دکمه‌ها برای اولین بار
    updateButtons();

    nextButton.addEventListener('click', () => {
        if (currentPageIndex < pages.length - 1) {
            // پنهان کردن صفحه فعلی
            pages[currentPageIndex].classList.remove('active');
            // افزایش اندیس صفحه
            currentPageIndex++;
            // نمایش صفحه جدید
            pages[currentPageIndex].classList.add('active');
            // بروزرسانی وضعیت دکمه‌ها
            updateButtons();
        } else {
            // در صفحه آخر، ارسال فرم (این قسمت را باید به نحو مناسبی تنظیم کنید)
            submitForm();
        }
    });

    prevButton.addEventListener('click', () => {
        if (currentPageIndex > 0) {
            // پنهان کردن صفحه فعلی
            pages[currentPageIndex].classList.remove('active');
            // کاهش اندیس صفحه
            currentPageIndex--;
            // نمایش صفحه جدید
            pages[currentPageIndex].classList.add('active');
            // بروزرسانی وضعیت دکمه‌ها
            updateButtons();
        }
    });


    // دریافت فیلد ورودی و دکمه
    const nameInput = document.getElementById("name");

    // تابع برای بررسی وضعیت ورودی
    const checkInput = () => {
        if (nameInput.value.trim() !== "") {
            nextButton.classList.add("hidden"); // مخفی کردن دکمه
        } else {
            nextButton.classList.remove("hidden"); // نمایش دکمه
        }
    };

    // افزودن رویداد 'input' به فیلد ورودی
    nameInput.addEventListener("input", checkInput);

    // تابع برای ارسال فرم (این بخش را به نحو مناسبی تنظیم کنید)
    function submitForm() {
        // این قسمت را باید به فرم شما و اطلاعات آن تطبیق دهید
        console.log("فرم ارسال شد!");
        // مثال: ارسال فرم به وب سرور
         document.getElementById("myForm").submit();
    }
});

// JavaScript for dynamically adding tank and nozzle fields
document.getElementById('gasoline_tanks').addEventListener('change', function() {
    var tankCount = parseInt(this.value);
    var container = document.getElementById('gasoline-tanks');
    container.innerHTML = '';
    for (var i = 1; i <= tankCount; i++) {
        container.innerHTML += `
            <div class="form-group">
                <input type="number" step="0.01" id="gasoline_tank_${i}" name="gasoline_tank_${i}" placeholder="موجوی مخزن بنزین ${i} " required>
                <label for="gasoline_tank_${i}">موجوی مخزن بنزین  ${i} </label>
            </div>
        `;
    }
});
    
    document.getElementById('gas_tanks').addEventListener('change', function() {
        var tankCount = parseInt(this.value);
        var container = document.getElementById('gas-tanks');
        container.innerHTML = '';
        for (var i = 1; i <= tankCount; i++) {
            container.innerHTML += `
                <div class="form-group">
                    <input type="number" step="0.01" id="gas_tank_${i}" name="gas_tank_${i}" placeholder="موجوی مخزن نفتگاز ${i}" required>
                    <label for="gas_tank_${i}">موجوی مخزن نفتگاز ${i}</label>
                </div>
            `;
        }
    });
    // Attach event listeners to 'change' events for the dropdowns
document.getElementById('gasoline_nozzles').addEventListener('change', function() {
    var nozzleCount = parseInt(this.value);
    var container = document.getElementById('gasoline-nozzles');
    container.innerHTML = '';

    // Create and append the input fields dynamically
    for (var i = 1; i <= nozzleCount; i++) {
        container.innerHTML += `
            <div class="form-group">
                <input type="number" step="0.01" id="gasoline_nozzle_${i}" name="gasoline_nozzle_${i}" placeholder="مقدار نازل بنزین ${i} " required>
                <label for="gasoline_nozzle_${i}">مقدار نازل بنزین ${i} </label>
            </div>
        `;
    }
});

document.getElementById('gas_nozzles').addEventListener('change', function() {
    var nozzleCount = parseInt(this.value);
    var container = document.getElementById('gas-nozzles');
    container.innerHTML = '';

    // Create and append the input fields dynamically
    for (var i = 1; i <= nozzleCount; i++) {
        container.innerHTML += `
            <div class="form-group">
                <input type="number" step="0.01" id="gas_nozzle_${i}" name="gas_nozzle_${i}" placeholder="مقدار نازل نفتگاز${i} " required>
                <label for="gas_nozzle_${i}">مقدار نازل نفتگاز ${i} </label>
            </div>
        `;
    }
});

// For gasoline nozzles
document.getElementById('gasoline_nozzles').addEventListener('change', function() {
    var nozzleCount = parseInt(this.value);
    var container = document.getElementById('gasoline-nozzlesT');
    container.innerHTML = '';

    // Create and append the input fields dynamically with result display
    for (var i = 0; i < nozzleCount; i++) {
        container.innerHTML += `
            <h6 class="text-start text-danger mt-4 ms-2 "><i class="bi bi-circle-fill fw-bold"></i> نازل ${i + 1}</h6>
            <div class="container-fluid ">
                <div class="row">
                    <div class="col-6 col-md-4">
                        <div class="form-group">
                            <input type="number" step="0.01" id="gasoline_nozzle_start_totalizer_${i}" name="gasoline_nozzle_start_totalizer_${i}" placeholder=" " class="" required>
                            <label for="gasoline_nozzle_start_totalizer_${i}"><small> توتالایزر ابتدا </small></label>
                        </div>
                    </div>
                    <div class="col-6 col-md-4">
                        <div class="form-group">
                            <input type="number" step="0.01" id="gasoline_nozzle_end_totalizer_${i}" name="gasoline_nozzle_end_totalizer_${i}" placeholder=" " class="" required>
                            <label for="gasoline_nozzle_end_totalizer_${i}"><small> توتالایزر انتها </small></label>
                        </div>
                    </div>
                    <div class="col-12 col-md-4 glasss mt-3">
                        <div class="result text-white fw-bold" id="gasoline_result_${i}">0</div>
                    </div>
                </div>
            </div>
        `;
    }

    // Attach event listeners to input fields to update results on input
    for (var i = 0; i < nozzleCount; i++) {
        document.getElementById(`gasoline_nozzle_start_totalizer_${i}`).addEventListener('input', function(event) {
            updateGasolineResults(event.target.id);
        });
        document.getElementById(`gasoline_nozzle_end_totalizer_${i}`).addEventListener('input', function(event) {
            updateGasolineResults(event.target.id);
        });
    }
});

// For gas nozzles
document.getElementById('gas_nozzles').addEventListener('change', function() {
    var nozzleCount = parseInt(this.value);
    var container = document.getElementById('gas-nozzlesT');
    container.innerHTML = '';

    // Create and append the input fields dynamically with result display
    for (var i = 0; i < nozzleCount; i++) {
        container.innerHTML += `
            <h6 class="text-start text-warning mt-4 ms-2 "><i class="bi bi-circle-fill fw-bold"></i> نازل ${i + 1}</h6>
            <div class="container-fluid ">
                <div class="row">
                    <div class="col-6 col-md-4">
                        <div class="form-group">
                            <input type="number" step="0.01" id="gas_nozzle_start_totalizer_${i}" name="gas_nozzle_start_totalizer_${i}" placeholder=" " class="" required>
                            <label for="gas_nozzle_start_totalizer_${i}"><small> توتالایزر ابتدا </small></label>
                        </div>
                    </div>
                    <div class="col-6 col-md-4">
                        <div class="form-group">
                            <input type="number" step="0.01" id="gas_nozzle_end_totalizer_${i}" name="gas_nozzle_end_totalizer_${i}" placeholder=" " class="" required>
                            <label for="gas_nozzle_end_totalizer_${i}"><small> توتالایزر انتها </small></label>
                        </div>
                    </div>
                    <div class="col-12 col-md-4 glasss mt-3">
                        <div class="result text-white fw-bold" id="gas_result_${i}">0</div>
                    </div>
                </div>
            </div>
        `;
    }

    // Attach event listeners to input fields to update results on input
    for (var i = 0; i < nozzleCount; i++) {
        document.getElementById(`gas_nozzle_start_totalizer_${i}`).addEventListener('input', function(event) {
            updateGasResults(event.target.id);
        });
        document.getElementById(`gas_nozzle_end_totalizer_${i}`).addEventListener('input', function(event) {
            updateGasResults(event.target.id);
        });
    }
});

// Function to update result based on inputs for gasoline 
function updateGasolineResults(inputId) {
    const i = inputId.split('_')[4]; // Extracting the index from the input ID
    const startInput = document.getElementById(`gasoline_nozzle_start_totalizer_${i}`);
    const endInput = document.getElementById(`gasoline_nozzle_end_totalizer_${i}`);
    const resultElement = document.getElementById(`gasoline_result_${i}`);

    const startValue = parseFloat(startInput.value) || 0;
    const endValue = parseFloat(endInput.value) || 0;

    const result = endValue - startValue;

    resultElement.textContent = `${result.toFixed(2)}`;
}

// Function to update result based on inputs for gas
function updateGasResults(inputId) {
    const i = inputId.split('_')[4]; // Extracting the index from the input ID
    const startInput = document.getElementById(`gas_nozzle_start_totalizer_${i}`);
    const endInput = document.getElementById(`gas_nozzle_end_totalizer_${i}`);
    const resultElement = document.getElementById(`gas_result_${i}`);

    const startValue = parseFloat(startInput.value) || 0;
    const endValue = parseFloat(endInput.value) || 0;

    const result = endValue - startValue;

    resultElement.textContent = `${result.toFixed(2)}`;
}



// Initialize Persian Date Picker --------------------------------------------------------------------------
$(document).ready(function() {
    // Initialize the Persian Datepicker for start_date and end_date fields
    $("#start_date").persianDatepicker();
    $("#end_date").persianDatepicker();
});