window.onload = function () {
    let container = document.getElementById("container");
    container.textContent = randomChars(0, 2); // 亂數生成 0 到 2 個字元
};

window.addEventListener("keyup", function (e) {
    let container = document.getElementById("container");
    console.log(e.key);
    
    // 檢查第一個字元是否與輸入相同，相同則刪除
    if (container.textContent.length > 0 && e.key === container.textContent[0]) {
        container.textContent = container.textContent.slice(1);
    }

    // 在字串後面新增 1 到 3 個隨機字元
    container.textContent += randomChars(1, 3);
});

function randomChars(min, max) {
    let count = Math.floor(Math.random() * (max - min + 1)) + min;
    let result = "";
    for (let i = 0; i < count; i++) {
        result += String.fromCharCode(97 + Math.floor(Math.random() * 26)); // 隨機 a-z
    }
    return result;
}