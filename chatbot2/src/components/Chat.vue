<template>

    <div id="app">
        <h1>Chat Message</h1>

        <textarea id="chat_textarea" rows="2" cols="50">
        </textarea>
        <div></div>
        <button type="button" @click="postMessage">Send</button>

        <p>{{inputText}}</p>
        <div>
            <br>
        </div>
        <h1>Chatbot Response</h1>
        <p>{{responseText}}</p>

    </div>
</template>


<script>
    import axios from 'axios';


    export default {
        name: 'Chat',

        props:['inputText','responseText'],

        methods: {
            chat(){
                const path = 'http://localhost:5000/ai_chat';
                //const path = 'http://localhost:5000/dummy_chat';
                console.log("here")
                console.log(this.inputText)
                axios.post(path,{'message':this.inputText})
                    .then((res) => {
                        this.responseText = res.data['message'];
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },

            postMessage(){
            //
                //this.inputText="Here"
                this.inputText=document.getElementById("chat_textarea").value
            //
                this.chat()
            },
            getMessage() {
                const path = 'http://localhost:5000/ping';
                axios.get(path)
                    .then((res) => {
                        this.msg = res.data;
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },
        },
        created() {
            this.getMessage();
        },
    };
</script>


<style scoped>

</style>