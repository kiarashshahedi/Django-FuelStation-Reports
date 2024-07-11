
// SHOW gasoline - gas - both ---------------------------------------------------------------------------------------

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
        element.classList.add('gg');
    });
    
    fuelElements.forEach(element => {
        element.style.display = 'none';
        if (element.tagName === 'INPUT') {
            element.value = '0';
        }
    });

    localStorage.setItem('fuelType', 'gas');
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
        element.classList.add('gg');
    });
    
    fuelElements.forEach(element => {
        element.style.display = 'block';
        if (element.tagName === 'INPUT') {
            element.value = '';
        }
    });

    localStorage.setItem('fuelType', 'petrol');
}

function showBoth() {
    let gasElements = document.querySelectorAll('.showGaz');
    let fuelElements = document.querySelectorAll('.showFuel');
    
    gasElements.forEach(element => {
        element.style.display = 'none';
        if (element.tagName === 'INPUT') {
            element.value = '0';
        }
    });
    fuelElements.forEach(element => {
        element.style.display = 'none';
        if (element.tagName === 'INPUT') {
            element.value = '0';
        }
    });
    BASE.forEach(element => {
        element.classList.remove('showBase');
        element.classList.add('gg');
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

    localStorage.setItem('fuelType', 'both');
}
// NEXT and PREVIEW buttons --------------------------------------------------------------------------------------

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

// JavaScript for dynamically adding tank and nozzle fields ---------------------------------------------------------

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
// NOZZLE number count -------------------------------------------------------------------------------------------

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

// For gasoline nozzles mount --------------------------------------------------------------------------------------

document.getElementById('gasoline_nozzles').addEventListener('change', function() {
    var nozzleCount = parseInt(this.value);
    var container = document.getElementById('gasoline-nozzlesT');
    container.innerHTML = '';

    // Create and append the input fields dynamically with result display
    for (var i = 0; i < nozzleCount; i++) {
        container.innerHTML += `
            <h6 class="text-start text-danger mt-4 ms-2 "><i class="bi bi-circle-fill fw-bold"></i> نازل ${i + 1}  بنزین </h6>
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

// For gas nozzles amount --------------------------------------------------------------------------------------------------

document.getElementById('gas_nozzles').addEventListener('change', function() {
    var nozzleCount = parseInt(this.value);
    var container = document.getElementById('gas-nozzlesT');
    container.innerHTML = '';

    // Create and append the input fields dynamically with result display
    for (var i = 0; i < nozzleCount; i++) {
        container.innerHTML += `
            <h6 class="text-start text-warning mt-4 ms-2 "><i class="bi bi-circle-fill fw-bold"></i> نازل ${i + 1}  نفتگاز </h6>
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

// Function to update result based on inputs for gasoline ------------------------------------------------------------

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

// Function to update result based on inputs for gas ------------------------------------------------------------------

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



// MAX and MIN for numbers input --------------------------------------------------------------------------

document.querySelectorAll('.MAX').forEach(function(input) {
    // اضافه کردن رویداد input به هر ورودی
    input.addEventListener('input', function() {
        let min = parseInt(input.min);
        let max = parseInt(input.max);
        let step = parseInt(input.step);
        let value = parseInt(input.value);
        
        if (value < min) {
            input.value = min;
        } else if (value > max) {
            input.value = max;
        } else if ((value - min) % step !== 0) {
            // در صورتی که مقدار وارد شده با step هماهنگ نباشد، آن را به نزدیکترین مقدار صحیح تنظیم کنید
            input.value = Math.round((value - min) / step) * step + min;
        }
    });
});


// fix buttom KEYboard ---------------------------------------------------------------------------------------------

// function adjustButtonPosition() {
//     const buttonContainer = document.getElementById('buttonContainer');
//     const viewportHeight = window.visualViewport.height;
//     const windowHeight = window.innerHeight;

//     if (viewportHeight < windowHeight) {
//         // Keyboard is open
//         const offset = windowHeight - viewportHeight;
//         buttonContainer.style.bottom = `${offset}px`;
//     } else {
//         // Keyboard is closed
//         buttonContainer.style.bottom = '0';
//     }
// }

// // Adjust on viewport resize
// window.visualViewport.addEventListener('resize', adjustButtonPosition);

// // Initial adjustment
// adjustButtonPosition();




// تاریخ شمسی -----------------------------------------------------------------------------------------------------

$(document).ready(function() {
    // Initialize the Persian Datepicker for start_date and end_date fields
    $("#start_date").persianDatepicker({
                    observer: true,
                    format: 'YYYY-MM-DD',
                    altField: '#start_date',
                    altFormat: 'YYYY-MM-DD',
                    onSelect: function(unixDate) {
                        var date = new persianDate(unixDate).toGregorian();
                        $('#start_date_gregorian').val(date.format('YYYY-MM-DD'));
                    }
                });

    $("#end_date").persianDatepicker({
            observer: true,
            format: 'YYYY-MM-DD',
            altField: '#end_date',
            altFormat: 'YYYY-MM-DD',
            onSelect: function(unixDate) {
                var date = new persianDate(unixDate).toGregorian();
                $('#end_date_gregorian').val(date.format('YYYY-MM-DD'));
            }
        });
});