 const apiKey = '####';

const knowledge_base = [
  {
    "intent": "Basic Features",
    "sub_intents": [
      {
        "sub_intent": "Video and Audio Calls",
        "steps": [
          "To start a video call, click on the \"Video\" button on the bottom left of the Zoom window.",
          "To start an audio call, click on the \"Audio\" button.",
          "During a call, you can mute or unmute your microphone by clicking on the \"Mute\" button.",
          "To turn on or off your video, click on the \"Video\" button."
        ]
      },
      {
        "sub_intent": "Screen Sharing",
        "steps": [
          "To share your screen, click on the \"Share Screen\" button.",
          "Select the window or application you want to share."
        ]
      },
      {
        "sub_intent": "Chat",
        "steps": [
          "To chat with others during the call, click on the \"Chat\" button.",
          "Type your message in the chat box and press Enter to send."
        ]
      },
      {
        "sub_intent": "Participants",
        "steps": [
          "To see the list of participants, click on the \"Participants\" button.",
          "You can mute or unmute individual participants by clicking on their names."
        ]
      }
    ]
  },
  {
    "intent": "Possible Problems and Solutions",
    "sub_intents": [
      {
        "sub_intent": "Audio Issues",
        "problem": "I can't hear other participants.",
        "solution": "Check your microphone settings and make sure it's not muted. If you're using a headset, make sure it's plugged in correctly."
      },
      {
        "sub_intent": "Video Issues",
        "problem": "My video is not visible to others.",
        "solution": "Check your camera settings and make sure it's not muted. If you're using a webcam, make sure it's plugged in correctly and not covered by an object."
      },
      {
        "sub_intent": "Connection Issues",
        "problem": "I can't connect to the meeting.",
        "solution": "Check your internet connection and try to reconnect. If the problem persists, try restarting Zoom or your computer."
      }
    ]
  },
  {
    "intent": "Advanced Features",
    "sub_intents": [
      {
        "sub_intent": "Recording",
        "steps": [
          "To record a meeting, go to the \"Meeting\" menu and select \"Record Meeting\".",
          "You can also start a cloud recording from within the meeting."
        ]
      },
      {
        "sub_intent": "Webinars",
        "steps": [
          "To host a webinar, go to the \"Webinar\" menu and select \"Start Webinar\".",
          "You can invite participants by sharing a registration link or by adding them manually."
        ]
      },
      {
        "sub_intent": "Breakout Rooms",
        "steps": [
          "To use breakout rooms, go to the \"Meeting\" menu and select \"Breakout Rooms\".",
          "You can create breakout rooms and assign participants to them."
        ]
      }
    ]
  },
  {
    "intent": "Troubleshooting",
    "steps": [
      "If you encounter any issues, check the Zoom status page (https://status.zoom.us/) to see if there are any known issues with the Zoom service.",
      "If the problem persists, contact Zoom support for help."
    ]
  }
];
function format_knowledge_base(knowledge_base) {
  return knowledge_base
    .map(({ question, answer }) => `- ${question}: ${answer}`)
    .join("\n");
}

// Assuming 'workflow.question' contains the user's question
const questions = workflow.question;

const prompt = `${questions}\n\nHere's some additional information that might be helpful:\n${format_knowledge_base(knowledge_base)}`;

const { data } = await axios.post(
  'https://api.openai.com/v1/chat/completions',
  {
    model: 'gpt-3.5-turbo-0301',
    messages: [
      { role: 'user', content: prompt },
      {
        role: 'system',
        content:
          'You are a professional IT expert at Kabarak University. Your task is to answer student questions, giving reference to Kabarak University in terms of URLs, organization names, and institutions where required. You should strictly answer the questions or give procedures to solve problems without adding or commenting on the answers given.'
      }
    ]
  },
  { headers: { Authorization: `Bearer ${apiKey}` } }
);

const reply = data.choices[0].message.content;

workflow.answergen = reply;
