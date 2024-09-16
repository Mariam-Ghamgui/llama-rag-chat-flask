<template>
  <div>
    <transition name="fade">
      <div v-if="showPopup" class="popup-wrapper">
        <div class="popup-message orange-popup">
          <p>Hey there 👋 <br><br>
          I can help you get information <br> about ENETCOM</p>
          <div class="white-popup"></div>
        </div>
      </div>
    </transition>

    <div v-if="!isWidgetOpen" class="chatbot-toggle" @click="toggleWidget">
      <img :src="botAvatar" alt="Chatbot Avatar" class="chatbot-avatar" />
    </div>

    <div v-if="isWidgetOpen" class="chatbot-widget">
      <div class="chatbot-header">
        EnetBot
        <div class="three-dots-menu">
          <font-awesome-icon icon="ellipsis-v" class="three-dots" @click="toggleMenu" />
          <div v-if="isMenuOpen" class="menu">
            <div class="menu-item" @click="closeChatbot">Close</div>
            <div class="menu-item" @click="clearChat">Clear</div>
          </div>
        </div>
      </div>
      <div class="chatbot-body">
        <div v-for="(message, index) in messages" :key="index" :class="['message', message.sender]">
          <div class="message-avatar" v-if="message.sender === 'bot'">
            <img :src="botAvatar" alt="Bot Avatar" />
          </div>
          <div class="message-bubble">{{ message.text }}</div>
          <div class="message-avatar" v-if="message.sender === 'user'">
            <img :src="userAvatar" alt="User Avatar" />
          </div>
        </div>
        <!-- Typing indicator bubble with avatar -->
        <div v-if="isTyping" class="message bot">
          <div class="message-avatar">
            <img :src="botAvatar" alt="Bot Avatar" />
          </div>
          <div class="message-bubble typing-indicator">
            <span class="dot"></span>
            <span class="dot"></span>
            <span class="dot"></span>
          </div>
        </div>
      </div>
      <div class="chatbot-footer">
        <input type="text" v-model="userMessage" @keyup.enter="sendMessage" placeholder="Type a message..." />
        <font-awesome-icon icon="paper-plane" class="send-icon" @click="sendMessage" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userMessage: '',
      messages: [],
      isMenuOpen: false,
      isWidgetOpen: false,
      showPopup: true,
      isTyping: false, 
      botAvatar: require('@/assets/botAvatar.png'),
      userAvatar: require('@/assets/userAvatar.png')
    };
  },
  methods: {
    toggleWidget() {
      this.isWidgetOpen = !this.isWidgetOpen;
      if (this.isWidgetOpen && this.messages.length === 0) {
        this.addBotMessage("Hi, how can I assist you today?");
      }
    },
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    closeChatbot() {
      this.isWidgetOpen = false;
      this.isMenuOpen = false;
    },
    clearChat() {
      this.messages = [];
      this.isMenuOpen = false;
      this.addBotMessage("Hi, how can I assist you today?");
    },
    addBotMessage(text) {
      this.messages.push({ sender: 'bot', text: text });
    },
    async sendMessage() {
    if (this.userMessage.trim() === '') return;

    const userMessageText = this.userMessage;
    this.messages.push({ sender: 'user', text: userMessageText });
    this.userMessage = '';

    this.isTyping = true;

    try {
        const response = await axios.post('http://localhost:5000/api/chat', {
            question: userMessageText 
        });

        this.isTyping = false;
        this.addBotMessage(response.data.response);
    } catch (error) {
        console.error('Error sending message to backend:', error);
        this.isTyping = false; 
        this.addBotMessage('Sorry, an error occurred.');
    }
}
  },
  mounted() {
    setTimeout(() => {
      this.showPopup = false;
    }, 2000);
  }
};
</script>

<style scoped>
.chatbot-widget {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  z-index: 1000; 
}
.chatbot-header {
  background-color: #0c356c;
  color: white;
  padding: 10px;
  text-align: center;
  font-weight: bold;
  position: relative;
}
.three-dots-menu {
  position: absolute;
  right: 10px;
  top: 10px;
}
.three-dots {
  font-size: 18px;
  cursor: pointer;
}
.menu {
  position: absolute;
  top: 30px;
  right: 0;
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
  z-index: 1000;
}
.menu-item {
  padding: 10px;
  cursor: pointer;
  color: #0c356c;
}
.menu-item:hover {
  background-color: #f0f0f0;
}
.chatbot-body {
  height: 300px;
  padding: 10px;
  overflow-y: auto;
  background-color: #f9f9f9;
}
.message {
  margin-bottom: 10px;
  display: flex;
  align-items: flex-end;
}
.message-bubble {
  display: inline-block;
  padding: 10px;
  border-radius: 15px;
  max-width: 80%;
  word-wrap: break-word;
}
.message.user {
  justify-content: flex-end;
}
.message.user .message-bubble {
  background-color: #ec6d07;
  color: white;
}
.message.bot {
  justify-content: flex-start;
}
.message.bot .message-bubble {
  background-color: #e3e7ee;
  color: black;
}
.message-avatar {
  margin: 0 5px;
}
.message-avatar img {
  width: 30px;
  height: 30px;
  border-radius: 50%;
}
.chatbot-footer {
  display: flex;
  padding: 10px;
  border-top: 1px solid #ccc;
}
.chatbot-footer input {
  flex: 1;
  padding: 5px;
  border: none;
  border-radius: 5px;
  outline: none;
}
.send-icon {
  margin-left: 5px;
  font-size: 20px;
  color: #0c356c;
  cursor: pointer;
}
.send-icon:hover {
  color: #004080;
}
.chatbot-toggle {
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 80px;
  height: 80px;
  background-color: #0c356c;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  z-index: 2000; 
}
.chatbot-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
}
.popup-wrapper {
  position: fixed;
  bottom: 0;
  right: 0; 
  z-index: 1000;
}
.popup-message {
  position: relative;
  background-color: #ec6d07;
  color: white;
  padding: 30px;
  border-radius: 400px 0 0 0; 
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  width: 350px;
  height: 350px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.white-popup {
  position: absolute;
  bottom: 0; 
  right: 0; 
  background-color: white;
  border-radius: 300px 0px 0px 0px; 
  width: 200px;
  height: 180px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
.typing-indicator {
  display: flex;
  align-items: center;
  justify-content: center;
}

.dot {
  width: 8px;
  height: 8px;
  margin: 0 2px;
  border-radius: 50%;
  background-color: #999;
  animation: bounce 0.6s infinite alternate;
}

.dot:nth-child(1) {
  animation-delay: 0s;
}

.dot:nth-child(2) {
  animation-delay: 0.2s;
}

.dot:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes bounce {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-10px);
  }
}

.message-avatar {
  margin-right: 5px; 
}
</style>