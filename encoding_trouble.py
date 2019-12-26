"""
utf8の全角チルダ「～」（EFBD9E） => cp932全角チルダ「～」（8160）
utf8の波ダッシュ「〜」（E3809C） => cp932全角チルダ「～」（8160）
utf8の全角マイナス「－」（EFBD9E） => cp932全角マイナス「－」（817c）
utf8の全角ハイフン「‐」（E3809C） => cp932全角ハイフン「‐」（815d）
"""

enc = "cp932"
#enc = "utf8"

msg = []
msg.append("～")
msg.append("〜")
msg.append("－")
msg.append("‐")
#msg.append("😀")
msg = "     ".join(msg)

f = open("file.txt", "w", encoding=enc)
f.writelines(msg)
f.close()

