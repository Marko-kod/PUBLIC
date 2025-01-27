const express = require("express");
const http = require("http");
const socketIo = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.use(express.static("public"));

let users = {};

io.on("connection", (socket) => {
    console.log("New user connected", socket.id);
    
    socket.on("joinChat", (username) => {
        users[socket.id] = username;
        io.emit("updateUsers", Object.values(users));
        socket.emit("chatWelcome", `Welcome to the chat, ${username}!`);
        socket.broadcast.emit("chatMessage", { user: "System", message: `${username} has joined the chat.` });
    });
    
    socket.on("sendMessage", (message) => {
        if (users[socket.id]) {
            io.emit("chatMessage", { user: users[socket.id], message });
        }
    });
    
    socket.on("disconnect", () => {
        if (users[socket.id]) {
            io.emit("chatMessage", { user: "System", message: `${users[socket.id]} has left the chat.` });
            delete users[socket.id];
            io.emit("updateUsers", Object.values(users));
        }
    });
});

server.listen(3000, () => {
    console.log("Chat server running on http://localhost:3000");
});
