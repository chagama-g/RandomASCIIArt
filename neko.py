import random


# original: https://2ch-aa.blogspot.com/2017/10/1010.html

neko = []

neko.append("""
　　　　　　　　 ,-､　　　　　　　　　　　　,.-､
　　　　　　　 ./:::::＼　　　　　　　　　 ／::::::ヽ
　　　　　　　/::::::::::::;ゝ--──-- ､._/::::::::::::::|
　　　　　　 /,.-‐''"´ 　　　　　　　　 ＼:::::::::::|
　　　　　／　 　　　　　　　　　　　　　　ヽ､::::|
　　　　/　　　　●　　　 　 　 　 　 　 　 　 ヽ|
　　 　 l　　　, , ,　　 　 　 　 　 　 ●　　　 　 l
　　　 .|　　　 　　　　(_人__丿　　　　　､､､　　|
　 　 　l　　　　　　　　　　　　　　　　　　　 　 l
　　　　` ､　　　　　　　　 　 　 　 　 　 　 　 /
　　　　　　`ｰ ､__　　　 　 　 　　　　　　　／
　　　　　　　　　/`'''ｰ‐‐──‐‐‐┬'''""´ """)
neko.append(
    """　　(・ω・´)⌒ゝ
　　とと二~⌒つ ～
　　　 　 　￣

　　　 ━━━━
""")

neko.append(
    """　　　　∧ ∧
　 (＿(,, ・∀・)　高猫♪
　⊆＿＿つつ

彡
"""
)

neko.append("""ミ
　　　　∧ ∧
　 )＿(,,　'A`)　　安猫
　⊆＿＿つつ""")

neko.append("""　∧,,∧
（=・ω・）　安猫にゃん
（,, ｕｕﾉ""")

neko.append("""　　　　　　　　　 　 |　　彡⌒ミ
　　　　　　　　　　　＼ (･ω･`　):: ふさふさだね…
　　　　　　　　　　　　　(|　　　|)::::
　　　　　　　　　　　　 　(γ　/:::::::
　 ∧_∧ 　　　　　　　　　し ＼:::
　.ﾐ,,・_・ﾐ　　　　　　　　　　　　 ＼
ヾ(,_ｕｕﾉ
　
　
　　　　　　　　　　　　　∧_∧ 　
　　　　　　　　　　　|　 ﾐ・_・,,ﾐ　　
　　　　　　　　　 　 |　　(ｕｕ._)～
　　　　　　　　　　　＼ (･ω･`　)::　 あ…ありがとう
　　　　　　　　　　　　　(|　　　|)::::
　　　　　　　　　　　　 　(γ　/:::::::
　　　　　　　　　　　　　　し ＼:::
　　　　　　　　　　　　　　　　　 ＼ 
""")

neko.append("""　　|＼＿／|
　　|―　― |
　　∧_∧_ノ_＿＿／/
　 (･ω･ )　　　　 /
　 O旦⊂|　 ＿　 ヽ
　 ＯＯノ_／｣/_／＼｣ ））））""")

neko.append("""
　　　　　　　わんわんお　　　　　　 　　　　./＼＿＿_／ヽ
　 　　　 　 　　, , - ー -､　　　　　　 　　 ／　 　 ||||　　　　＼　
　　　　　, -'ｌ´ 　　　 　 　 ' ､　　 　　 　 / 　　　 　　 　　 　　ヽ　
　　　　/　　l　　/ヽ　 　/ヽ ヽ　 　 　　 l 　　　/ヽ 　　 /ヽ　　 l　
　　　　ｌ　　 l⊂⊃　　　　　⊂⊃　 　　 |　 三 　　　　　 　三　|　にゃんにゃんお　
　　　　l　　 l　 　 (__人__)　　,'　 　　 　　'、　　 （__人__）　　　/　　
　　　　ヽ__/,,,,,　　　　　,,,,,,,,ノ　　　　　　　｀;,,,,,,,,　　　　　,,,,,,,,'
　　　　　/　,､,,))　　　((_,,、 ﾞヽ　　　　　　/　,､,,))　　　((_,,、 ﾞヽ
　　　　￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣""")

neko.append("""　　　　　　　　彡⌒ミ
　　　　　　　('(ﾟ∀ﾟ*)∩　 おもいよ！
　　　　／⌒⌒⌒⌒⌒ヽ
　　 ／ ﾊ_ﾊ　♪... 　／ 　おやすみー♪
　／　(,,・д・),,)～／
（＿＿＿＿＿ _ノ


　　　　　　　　彡⌒ミ
　　　　　　　　(ｰωｰ )　　 ZZZ・・・
　　　　／⌒⌒⌒⌒∪ヽ
　　 ／ ﾊ_ﾊ　zzz... 　／ 　
　／　(,,-д-),,)～／
（＿＿＿＿＿ _ノ""")

neko.append("""　　　　　 ∧,,∧
　　　　　(,,・∀・)ﾆｬｰ
　　　　～(_ｕ,ｕﾉ
　　　　　彡 ⌒ ミ
　　　　 ∩´･ω･`∩
　　　　 ヽ 　　　ﾉ　　かわいい
　　　　 ｜ ｜　|　　
　　　　 （_＿）＿）""")

neko.append("""　 　 　 　 　 　 　 　 彡⌒ ミ
　 　 　 　 　 　 　 　 (･ω･´)⌒ゝ
　 　 　 　 　 　 　 　 とと二~⌒つ ～
　 　 　 　 　 　 　 　 　 　 　￣

　 　 　 　 　 　 　 　 　 ━━━



| ☆
|〃
|彡⌒ ミ
|(>ω<´)⌒ゝ
|とと二~⌒つ ～
|　 　 　￣
|
　 ━━━""")

neko.append("""
　　　　　 ∧,,∧
　　　　　(,,・∀・)
　　　　～(_ｕ,ｕﾉ""")

neko.append("""
　 　 　　 ,-､　　　　　　　　　　　 　,.-､
　　　　 ./:::::＼　　　　　　　　　 ／::::::ヽ
　　　　/::::::::::::;ゝ--──-- ､._/::::::::::::::|
　　　 /,.-‐''"´ 　　　　　　　　 ＼:::::::::::|
　　／　 　　　　　　　　　　　　　　ヽ､::::|
　/　　　　　　　　　　　　　　　　　　　ヽ|
　l　　　　　　　　　　　　 　 　 　 　 　 　 l
. |　　　 ●　　　　　　　　　　　　　　　　　|
　l　　, , ,　　　　　　　　　　　●　　　　 　l
　` ､　　　　　　(__人__丿　　　　､､､ 　 /
　　　`ｰ ､__　　　　　　　 　　 　　　 ／
　　　　　　　/`'''ｰ‐‐──‐‐‐┬'''""´
　　　　　　 /,　　　　　　　　　　|
　　　　　 (_/　 　　　　 　 　|　　|
　　　 　　　 , 　　　　　　　 ヽ、_） 　　∩
　　　　　　　l　　　　 　 　 　　|＼　　ﾉ |　　 　
　.　　　 　　 |　　　 ヘ 　　 　 |｀ヽ二 ノ
　.　 　 　 　 |　　 /　 ＼　 　 /
　　　　　　　｀ｰ‐'　　　 ｀ー‐'""")


if __name__ == "__main__":
    index = int(random.uniform(0, len(neko)))
    print(neko[index])
