// 1) indentation
// 2) function

const root = ReactDOM.createRoot(document.getElementById("root"));

function Header() {
    return React.createElement(
        "header",
        { style: { backgroundColor: "#eee", padding: "10px", textAlign: "center" } },
        React.createElement('h1', null, "Welcome to React"),
        React.createElement('p', null, "lorem ipsum... wedpiwepid")
    );
}

function Main() {
    return React.createElement(
        "main",
        { style: { padding: "20px" } },
        React.createElement("h2", null, "Good things about right"),
        React.createElement(
            "ul",
            null,
            React.createElement("li", null, "reactivity"),
            React.createElement("img", { src: "GOA-Homeworks/Day-0138/hw/image.png" }),
            React.createElement("button", null, "press")
        ),
        React.createElement(
        "div",
        { style: { border: "2px solid blue", padding: "10px", marginTop: "10px" } },
        React.createElement(
        "div",
        { style: { border: "2px solid lightblue", padding: "10px" } },
        React.createElement(
          "div",
          { style: { border: "2px solid skyblue", padding: "10px" } },
          React.createElement("p", null, "3")
        )
      )
    ),
    
    );
}

function Footer() {
    return React.createElement(
        "footer",
        { style: { background: "#eee", padding: "10px", textAlign: "center" } },
        React.createElement("small", null, "© 2025 My First React Project")
    );
}

function App() {
    return React.createElement(
        "div",
        null,
        Header(),
        Main(),
        Footer(),
    );
}

root.render(App());