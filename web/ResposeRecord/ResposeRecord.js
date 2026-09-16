const recordButton = document.getElementById("record-button");

recordButton.addEventListener("click", function () {

    const responseContent =
        document.getElementById("response-content").value;

    // 対応内容が入力されているか確認
    if (responseContent.trim() === "") {
        alert("対応内容を入力してください。");
        return;
    }

    // 現在はダミー処理
    alert("対応を記録しました。");

});