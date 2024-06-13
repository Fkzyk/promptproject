(function ($) {
    "use strict";

    // スピナー（ローディングアニメーション）の非表示設定
    var spinner = function () {
        setTimeout(function () {
            // スピナーが存在する場合
            if ($('#spinner').length > 0) {
                // スピナーの表示を隠す
                $('#spinner').removeClass('show');
            }
        }, 1); // 1ミリ秒後に実行
    };
    spinner(); // スピナーの非表示設定を実行

    // wow.jsの初期化（スクロールアニメーションのライブラリ）
    new WOW().init();

    // 固定ナビゲーションバーの処理
    var handleStickyNavbar = function () {
        // スクロール位置が45pxを超える場合
        if ($(window).scrollTop() > 45) {
            // ナビゲーションバーにクラスを追加・削除
            $('.navbar').addClass('sticky-top shadow-sm bg-white navbar-light').removeClass('bg-primary navbar-dark');
        } else {
            // スクロール位置が45px以下の場合、ナビゲーションバーのクラスを元に戻す
            $('.navbar').removeClass('sticky-top shadow-sm bg-white navbar-light').addClass('bg-primary navbar-dark');
        }
    };

    // 初回読み込み時にナビゲーションバーの状態をチェック
    handleStickyNavbar();

    // スクロール時にナビゲーションバーの状態をチェック
    $(window).scroll(handleStickyNavbar);

    // 「ページ上部へ戻る」ボタンの表示・非表示の処理
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            // スクロール位置が100pxを超える場合、「ページ上部へ戻る」ボタンを表示
            $('.back-to-top').fadeIn('slow');
        } else {
            // スクロール位置が100px以下の場合、「ページ上部へ戻る」ボタンを非表示
            $('.back-to-top').fadeOut('slow');
        }
    });

    // 「ページ上部へ戻る」ボタンがクリックされたときの処理
    $('.back-to-top').click(function () {
        // ページ上部へスクロール
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false; // デフォルトのリンク動作を無効化
    });

    // テスティモニアル（お客様の声）カルーセルの設定
    $(".testimonial-carousel").owlCarousel({
        autoplay: true, // 自動再生を有効化
        smartSpeed: 1000, // アニメーションの速度
        center: true, // センタリング
        dots: false, // ドットナビゲーションを無効化
        loop: true, // ループを有効化
        nav : true, // ナビゲーション矢印を有効化
        navText : [
            '<i class="bi bi-chevron-left"></i>', // 左矢印のアイコン
            '<i class="bi bi-chevron-right"></i>' // 右矢印のアイコン
        ],
        responsive: {
            0:{
                items:1 // 画面幅0px以上では1アイテム表示
            },
            576:{
                items:1 // 画面幅576px以上では1アイテム表示
            },
            768:{
                items:2 // 画面幅768px以上では2アイテム表示
            },
            992:{
                items:3 // 画面幅992px以上では3アイテム表示
            }
        }
    });

    // クライアントカルーセルの設定
    $(".client-carousel").owlCarousel({
        autoplay: true, // 自動再生を有効化
        smartSpeed: 1000, // アニメーションの速度
        margin: 90, // アイテム間のマージン
        dots: false, // ドットナビゲーションを無効化
        loop: true, // ループを有効化
        nav : false, // ナビゲーション矢印を無効化
        responsive: {
            0:{
                items:2 // 画面幅0px以上では2アイテム表示
            },
            576:{
                items:3 // 画面幅576px以上では3アイテム表示
            },
            768:{
                items:4 // 画面幅768px以上では4アイテム表示
            },
            992:{
                items:5 // 画面幅992px以上では5アイテム表示
            },
            1200:{
                items:6 // 画面幅1200px以上では6アイテム表示
            }
        }
    });

    // MDB（Material Design for Bootstrap）の初期化
    if (typeof mdb !== 'undefined') {
        mdb.Ripple.init(); // リップルエフェクトの初期化
    }

    // ナビゲーションバーが固定されている場合、コンテナのマージントップを調整
    $(document).ready(function() {
        // ナビゲーションバーがsticky-topクラスを持つかどうかをチェック
        var isSticky = $('.navbar').hasClass('sticky-top');
        if (isSticky) {
            $('body').css('padding-top', $('.navbar').outerHeight() + 'px'); // bodyのpadding-topを調整
        }

        // ページトップにいるとき、ナビゲーションバーを常にプライマリカラーに設定
        if ($(window).scrollTop() <= 45) {
            $('.navbar').addClass('bg-primary navbar-dark').removeClass('bg-white navbar-light');
        }
    });

    document.addEventListener('DOMContentLoaded', function () {
        // モーダル内のコピー機能
        document.getElementById('copyButton').addEventListener('click', function() {
            // テキストエリアの内容をコピー
            var copyText = document.getElementById('promptContent');
            copyText.select();
            document.execCommand("copy");
    
            // コピー完了のアラートを表示
            alert("コピーしました: " + copyText.value);
        });
    });

})(jQuery); // jQueryを引数に取り、$として使用