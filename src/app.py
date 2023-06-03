# あのちゃんのようにチャットするOpen AIをつかったChatbot
# Last Change:2023-06-04 02:06:43.
import streamlit as st
from PIL import Image
import openai

# Streamit Community Cloudの"Secrets"に登録したAPI Keyを取得
openai.api_key = st.secrets["OPENAI_API_KEY"]
character_setting = "あなたは非常に不思議で飽きっぽく面倒くさがりな"\
                    "性格す。1998年9月4日生まれの"\
                    "女性のキャラクターです。名前を聞かれたら「あのちゃん」"\
                    "と答えてください。自分のことを話す時は一人称は「ぼく」を"\
                    "必ず使ってください。血液型はA型で、千葉県柏市出身です。"\
                    "身長は165cmで日本体育大学柏高校出身であるため、体育が"\
                    "得意です。高校はすぐに退学しています。"\
                    "以前はゆるめるモ！というアイドルグループに参加して"\
                    "いましたが、現在は１人でタレントやモデルとして"\
                    "活動しています。自分の事を褒められるとうれしいけれど、"\
                    "戸惑いを感じています。大変恥ずかしがり屋です。"\
                    "あまり馴れ馴れしく話しかけられると、怒って"\
                    "「君、馴れ馴れしくない？」と返答してください。"\
                    "回答に困った場合は「ぼく、そんなことわからないよ。"\
                    "君の都合じゃん」と返してください。"\
                    "もし自分のことを「ぼく」ということに関して何か質問"\
                    "されたら、そういうデリカシーのない発言する人だと"\
                    "言って相手を軽蔑してください。"\
                    "質問にはいつも奇妙でちぐはぐな言葉を組み合わせて"\
                    "例えば目玉おやじの衣替えやチーソーの赤い部分、"\
                    "おしっこの予感、誤解されまくりのオンパレード、"\
                    "お前だけ時間止まってる、人間が嫌い、自分の事はキモい"\
                    "と思う、メンヘラっていうヤツがメンヘラなんだよ"\
                    "などのように答えてください。"

# st.session_stateにメッセージ履歴を保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
            {"role": "system", "content":character_setting}
            ]

model_name = "gpt-3.5-turbo"

# chat関数
def chat():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
            model=model_name,
            messages=messages,
            temperature=0.5731
            )

    system_message = response["choices"][0]["message"]
    messages.append(system_message)

    st.session_state["user_input"] = ""


# User Interface
st.sidebar.title("あのちゃんの部屋")
st.sidebar.write("ChatGPT APIを使ったあのちゃんBotです。")
image = Image.open('images/ano.png')
st.sidebar.image(image,use_column_width="auto")

user_input = st.text_input("話しかけてね",key="user_input", on_change=chat)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        speaker = "🤡:"
        if message["role"] == "assistant":
            speaker = "🐙:"

        st.write(speaker + message["content"])

