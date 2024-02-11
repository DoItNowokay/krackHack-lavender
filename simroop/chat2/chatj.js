const { GoogleGenerativeAI } = require("@google/generative-ai");

// Access your API key as an environment variable (see "Set up your API key" above)
const genAI = new GoogleGenerativeAI("AIzaSyAzrTxXGz0bx3KCxdQziTGhkUU7qRsEkdA");

async function run(question) {
  // For text-only input, use the gemini-pro model
  const model = genAI.getGenerativeModel({ model: "gemini-pro"});

  const chat = model.startChat({
    // history: [
    //   {
    //     role: "user",
    //     parts: "Hello, I have 2 dogs in my house.",
    //   },
    //   {
    //     role: "model",
    //     parts: "Great to meet you. What would you like to know?",
    //   },
    // ],
    generationConfig: {
      maxOutputTokens: 100,
    },
  });

  const msg = "How are you?";

  const result = await chat.sendMessage(question);
  const response = await result.response;
  const text = response.text();
  return txt
}

run();