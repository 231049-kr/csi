// 通知切り替えボタンを取得
const tabs = document.querySelectorAll(".tab");


// 通知をすべて取得
const notifications = document.querySelectorAll(".notification");


// 未対応件数を表示する場所を取得
const unhandledCount = document.querySelector("#unhandled-count");



// ========================================
// 未対応件数を数える
// ========================================

function updateCount() {

    let count = 0;

    notifications.forEach(notification => {

        // 通知の状態を取得
        const status = notification.dataset.status;

        // 未対応ならカウント
        if (status === "unhandled") {
            count++;
        }

    });

    // HTMLに件数を表示
    unhandledCount.textContent = count;
}



// ========================================
// タブのクリック処理
// ========================================

tabs.forEach(tab => {

    tab.addEventListener("click", () => {


        // 押されたボタンの種類を取得
        const filter = tab.dataset.filter;


        // --------------------------------
        // ボタンの選択状態を変更
        // --------------------------------

        tabs.forEach(t => {
            t.classList.remove("active");
        });

        tab.classList.add("active");


        // --------------------------------
        // 通知の表示・非表示
        // --------------------------------

        notifications.forEach(notification => {


            // 通知の状態を取得
            const status = notification.dataset.status;


            // 「すべて」の場合
            if (filter === "all") {

                notification.style.display = "flex";

            }


            // ボタンと通知の状態が一致する場合
            else if (filter === status) {

                notification.style.display = "flex";

            }


            // それ以外の場合
            else {

                notification.style.display = "none";

            }

        });

    });

});



// ========================================
// ページ読み込み時に未対応件数を表示
// ========================================

updateCount();