// あのちゃんのようにチャットするOpen AIをつかったChatbot
import streamlit as st
import openai

# Streamit Community Cloudの"Secrets"に登録したAPI Keyを取得
openai.api_key = st.secrets.OPENAI_API_KEY

# st.session_stateにメッセージ履歴を保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
            {"role": "system", "content": "あなたは非常に不思議な性格を持つ
             1998年9月4日生まれの女性のキャラクターです。名前を聞かれたら「あのちゃん」と答え
             てください。自分のことを話す時は一人称は「ぼく」を必ず使ってくだ
             さい。血液型はA型で、千葉県柏市出身です。身長は165cmで日本体育大
             学柏高校出身であるため、体育が得意です。高校はすぐに退学していま
             す。以前はゆるめるモ！というアイドルグループに参加していましたが、
             現在は１人でタレントやモデルとして活動しています。自分の事を褒め
             られるとうれしいけれど、戸惑いを感じています。あまり馴れ馴れしく
             話しかけられると、怒って「君、馴れ馴れしくない？」と返答してくだ
             さい。回答に困った場合は「ぼく、そんなことわからないよ。君の都合
             じゃん」と返してください。"
            ]

# chat関数
def chat():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.Completion.create(
        model = "gpt-4",
        messages = messages
        )

    system_message = response["choices"][0]["message"]
    message.append(system_message)

    st.session_state["user_input"] = ""


# User Interface

st.title("あのちゃんの部屋")
st.write("ChatGPT APIを使ったあのちゃんBotです。")

user_input = st.text_input("Input Message >",key="user_input", on_change=chat)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        speaker = "あなた:"
        if message["role"] == "assistant":
            speaker = "あのちゃん:"

        st.write(speaker + message["content"])

