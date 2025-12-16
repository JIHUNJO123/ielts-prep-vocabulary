import json

new_strings = {
    'en': {
        'privacyPolicyContent': 'This app does not collect, store, or share any personal information.\n\nYour learning progress and favorites are stored only on your device.\n\nNo data is transmitted to external servers.',
        'restorePurchaseDesc': 'If you have previously purchased ad removal on another device or after reinstalling the app, tap here to restore your purchase.',
        'restoreComplete': 'Restore complete',
        'noPurchaseFound': 'No previous purchase found'
    },
    'ko': {
        'privacyPolicyContent': '이 앱은 개인정보를 수집, 저장 또는 공유하지 않습니다.\n\n학습 진도와 즐겨찾기는 기기에만 저장됩니다.\n\n외부 서버로 데이터가 전송되지 않습니다.',
        'restorePurchaseDesc': '다른 기기에서 광고 제거를 구매했거나 앱을 재설치한 경우, 여기를 눌러 구매를 복원하세요.',
        'restoreComplete': '복원 완료',
        'noPurchaseFound': '이전 구매 내역이 없습니다'
    },
    'ja': {
        'privacyPolicyContent': 'このアプリは個人情報を収集、保存、共有しません。\n\n学習の進捗とお気に入りはデバイスにのみ保存されます。\n\n外部サーバーへのデータ送信はありません。',
        'restorePurchaseDesc': '別のデバイスで広告削除を購入した場合、またはアプリを再インストールした場合は、ここをタップして購入を復元してください。',
        'restoreComplete': '復元完了',
        'noPurchaseFound': '以前の購入が見つかりません'
    },
    'zh': {
        'privacyPolicyContent': '本应用不会收集、存储或分享任何个人信息。\n\n您的学习进度和收藏仅存储在您的设备上。\n\n不会向外部服务器传输任何数据。',
        'restorePurchaseDesc': '如果您之前在其他设备上购买了去广告功能，或重新安装了应用，请点击此处恢复购买。',
        'restoreComplete': '恢复完成',
        'noPurchaseFound': '未找到之前的购买记录'
    },
    'es': {
        'privacyPolicyContent': 'Esta aplicación no recopila, almacena ni comparte ninguna información personal.\n\nTu progreso de aprendizaje y favoritos se almacenan solo en tu dispositivo.\n\nNo se transmiten datos a servidores externos.',
        'restorePurchaseDesc': 'Si compraste la eliminación de anuncios en otro dispositivo o después de reinstalar la aplicación, toca aquí para restaurar tu compra.',
        'restoreComplete': 'Restauración completada',
        'noPurchaseFound': 'No se encontró compra anterior'
    },
    'fr': {
        'privacyPolicyContent': "Cette application ne collecte, ne stocke ni ne partage aucune information personnelle.\n\nVotre progression et vos favoris sont stockés uniquement sur votre appareil.\n\nAucune donnée n'est transmise aux serveurs externes.",
        'restorePurchaseDesc': "Si vous avez précédemment acheté la suppression des publicités sur un autre appareil ou après avoir réinstallé l'application, appuyez ici pour restaurer votre achat.",
        'restoreComplete': 'Restauration terminée',
        'noPurchaseFound': 'Aucun achat précédent trouvé'
    },
    'de': {
        'privacyPolicyContent': 'Diese App sammelt, speichert oder teilt keine persönlichen Daten.\n\nIhr Lernfortschritt und Ihre Favoriten werden nur auf Ihrem Gerät gespeichert.\n\nEs werden keine Daten an externe Server übertragen.',
        'restorePurchaseDesc': 'Wenn Sie die Werbeentfernung zuvor auf einem anderen Gerät gekauft oder die App neu installiert haben, tippen Sie hier, um Ihren Kauf wiederherzustellen.',
        'restoreComplete': 'Wiederherstellung abgeschlossen',
        'noPurchaseFound': 'Kein früherer Kauf gefunden'
    },
    'pt': {
        'privacyPolicyContent': 'Este aplicativo não coleta, armazena ou compartilha nenhuma informação pessoal.\n\nSeu progresso de aprendizado e favoritos são armazenados apenas no seu dispositivo.\n\nNenhum dado é transmitido para servidores externos.',
        'restorePurchaseDesc': 'Se você comprou a remoção de anúncios em outro dispositivo ou após reinstalar o aplicativo, toque aqui para restaurar sua compra.',
        'restoreComplete': 'Restauração concluída',
        'noPurchaseFound': 'Nenhuma compra anterior encontrada'
    },
    'vi': {
        'privacyPolicyContent': 'Ứng dụng này không thu thập, lưu trữ hoặc chia sẻ bất kỳ thông tin cá nhân nào.\n\nTiến độ học tập và mục yêu thích của bạn chỉ được lưu trữ trên thiết bị của bạn.\n\nKhông có dữ liệu nào được truyền đến máy chủ bên ngoài.',
        'restorePurchaseDesc': 'Nếu bạn đã mua tính năng xóa quảng cáo trên thiết bị khác hoặc sau khi cài đặt lại ứng dụng, hãy nhấn vào đây để khôi phục giao dịch mua.',
        'restoreComplete': 'Khôi phục hoàn tất',
        'noPurchaseFound': 'Không tìm thấy giao dịch mua trước đó'
    },
    'ar': {
        'privacyPolicyContent': 'هذا التطبيق لا يجمع أو يخزن أو يشارك أي معلومات شخصية.\n\nيتم تخزين تقدم التعلم والمفضلات على جهازك فقط.\n\nلا يتم نقل أي بيانات إلى خوادم خارجية.',
        'restorePurchaseDesc': 'إذا كنت قد اشتريت إزالة الإعلانات سابقًا على جهاز آخر أو بعد إعادة تثبيت التطبيق، انقر هنا لاستعادة مشترياتك.',
        'restoreComplete': 'تم الاستعادة',
        'noPurchaseFound': 'لم يتم العثور على مشتريات سابقة'
    }
}

langs = ['ko', 'ja', 'zh', 'es', 'fr', 'de', 'pt', 'vi', 'ar']
for lang in langs:
    path = f'lib/l10n/app_{lang}.arb'
    with open(path, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    data.update(new_strings.get(lang, new_strings['en']))
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'{lang} updated')
print('Done')
