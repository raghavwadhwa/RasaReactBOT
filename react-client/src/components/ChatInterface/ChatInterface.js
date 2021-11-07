import "./ChatInterface.css";

import React, { Fragment, useState, useEffect, useRef } from "react";
import { v4 as uuidv4 } from "uuid";
import AudioReactRecorder, { RecordState } from "audio-react-recorder";
import { Howl } from "howler";

import botimg from "./static/logo.png";
import userimg from "./static/user.png";
import toggleimg from "./static/favicon.svg";

import CancelIcon from "@mui/icons-material/Cancel";
import PauseCircleIcon from "@mui/icons-material/PauseCircle";
import PlayCircleFilledWhiteIcon from "@mui/icons-material/PlayCircleFilledWhite";
import StopCircleIcon from "@mui/icons-material/StopCircle";

import axios from "axios";

const ChatInterface = () => {
  const [toggleState, setToggleState] = useState(false);
  const [recordState, setRecordState] = useState(null);
  const [chats, setChats] = useState([]);
  const messagesEndRef = useRef(null);
  const [toastVisible, setToastVisible] = useState(true);
  // const [audioURL, setAudioURL] = useState("");

  const soundPlay = (url) => {
    console.log(url);
    const sound = new Howl({
      src: [url],
      html5: true,
    });
    sound.play();
  };

  const toggleHandler = () => {
    setToggleState(!toggleState);
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    console.log(chats);
    scrollToBottom();
  }, [chats]);

  useEffect(() => {
    setChats([
      {
        id: uuidv4(),
        type: "bot",
        msg: "Hello I am Myntra VoiceBot! How can i help u?",
      },
    ]);

    setTimeout(() => {
      setToastVisible(false);
    }, 5000);
  }, []);

  const addChatToUI = (msg, type) => {
    const dataToAdd = {
      id: uuidv4(),
      type: type,
      msg: msg,
    };
    setChats((oldArray) => [...oldArray, dataToAdd]);
  };

  const start = () => {
    setRecordState(RecordState.START);
  };

  const stop = () => {
    setRecordState(RecordState.STOP);
  };

  const pause = () => {
    setRecordState(RecordState.PAUSE);
  };

  const onStop = (audioData) => {
    // console.log("audioData", audioData);

    //create form data
    let formdata = new FormData();
    formdata.append("file", audioData.blob, "file.wav");
    //translate text
    axios
      .post("http://localhost:8000/translate/", formdata, {
        headers: {
          "content-type": "multipart/form-data",
        },
      })
      .then((resJSON) => {
        // console.log("translate => ", resJSON.data.msg);
        addChatToUI(resJSON.data.msg, "user");

        //get result
        setTimeout(() => {
          axios
            .post("http://localhost:8000/response/", {
              msg: resJSON.data.msg,
              lang: resJSON.data.lang,
            })
            .then((resJSON) => {
              console.log("response => ", resJSON.data.msg);
              addChatToUI(resJSON.data.msg, "bot");
              // setAudioURL(resJSON.audiourl);
              soundPlay(resJSON.data.url);
            });
        }, 200);
      });
  };

  return (
    <Fragment>
      <div class="background">
        <div class="container">
          <div class="panel pricing-table">
            <div class="pricing-plan">
              {/* <img
                src="https://s22.postimg.cc/8mv5gn7w1/paper-plane.png"
                alt=""
                class="pricing-img"
              /> */}
              <h2 class="pricing-header">React-Client</h2>
              <ul class="pricing-features">
                <li class="pricing-features-item">Voice Bot User Interface</li>
                <li class="pricing-features-item">Records User Audio</li>
                <li class="pricing-features-item">Sends Blob to Django API</li>
                <li class="pricing-features-item">Plays audio URL received</li>
              </ul>
            </div>

            <div class="pricing-plan">
              {/* <img
                src="https://s28.postimg.cc/ju5bnc3x9/plane.png"
                alt=""
                class="pricing-img"
              /> */}
              <h2 class="pricing-header">Django-API</h2>
              <ul class="pricing-features">
                <li class="pricing-features-item">Receives Audio Blob</li>
                <li class="pricing-features-item">Detects Audio Language</li>
                <li class="pricing-features-item">Transcribes Audio</li>
                <li class="pricing-features-item">Get RASA Response</li>
                <li class="pricing-features-item">Generate Audio Response</li>
              </ul>
            </div>

            <div class="pricing-plan">
              {/* <img
                src="https://s21.postimg.cc/tpm0cge4n/space-ship.png"
                alt=""
                class="pricing-img"
              /> */}
              <h2 class="pricing-header">RASA-Server</h2>
              <ul class="pricing-features">
                <li class="pricing-features-item">Greetings</li>
                <li class="pricing-features-item">
                  Subscription, Sales, FAQ's
                </li>
                <li class="pricing-features-item">Orders Information</li>
                <li class="pricing-features-item">Cart Related Queries</li>
                <li class="pricing-features-item">Product Queries</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <div id="Smallchat">
        <div
          className={`Layout Layout-open ${
            !toggleState && "Layout-expand"
          } Layout-right`}
        >
          <div className="Messenger_messenger">
            <div className="Messenger_header">
              <div className="Messenger_prompt">How can we help you?</div>
              <span className="chat_close_icon" onClick={toggleHandler}>
                <CancelIcon />
              </span>
            </div>
            <div className="Messenger_content" id="chatcontainer">
              <div className="Messages chats" id="chats">
                {chats.map((chat) => {
                  return (
                    <div>
                      <div key={uuidv4()}>
                        <img
                          className={
                            chat.type === "bot" ? "botAvatar" : "userAvatar"
                          }
                          alt="logo"
                          src={chat.type === "bot" ? botimg : userimg}
                        />
                        <p
                          className={chat.type === "bot" ? "botMsg" : "userMsg"}
                        >
                          {chat.msg}
                        </p>
                      </div>
                      <div className="clearfix"></div>
                    </div>
                  );
                })}
                <div className="clearfix"></div>
                <div ref={messagesEndRef} />
              </div>
              <div className="Input Input-blank">
                <AudioReactRecorder
                  state={recordState}
                  onStop={onStop}
                  backgroundColor={`white`}
                  foregroundColor={`#F13AB1`}
                  canvasWidth={300}
                  canvasHeight={70}
                />
                <div className="controls">
                  <div onClick={pause} className="pause">
                    <PauseCircleIcon fontSize={`large`} />
                  </div>
                  <div onClick={start}>
                    <PlayCircleFilledWhiteIcon
                      className="start"
                      fontSize={`large`}
                      style={{ fontSize: 50 }}
                    />
                  </div>
                  <div onClick={stop} className="stop">
                    <StopCircleIcon fontSize={`large`} />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div
          className={`toast ${!toastVisible && "toast-invisible"}`}
          role="alert"
          aria-live="assertive"
          aria-atomic="true"
          data-animation="true"
          data-delay="8000"
        >
          <div className="toast-header">
            <strong>Welcome to Myntra 👋</strong>
          </div>
        </div>
        <div className="chat_on" onClick={toggleHandler}>
          <img className="iconic" alt="logo" src={toggleimg} />
        </div>
      </div>
    </Fragment>
  );
};

export default ChatInterface;
