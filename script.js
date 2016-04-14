/*
    Fill this array with a list of names of images
    to be pre-loaded.
*/
var preload = [
  "wheat.png" 
];

/*
    This section pre-loads your images.
    Don't change it unless you know what you're doing.
*/
var preloadObj = new Array(preload.length);
for (var i = 0; i < preload.length; i++)
{
    preloadObj[i] = new Image();
    preloadObj[i].src = preload[i];
}

/* Declare variables for characters, positions, and text blocks here */
var script; // this variable will hold your script

var n; // short for "narrator"
var inputArea;
inputArea = new Input('inputLogin', {
	position: new Position(0.2, 0.5),
	width: 0.5,
	text: "Digite seu login"
});
var inputLogin;
var spreadsheetID = "SPREADSHEET KEY";
var url = "https://spreadsheets.google.com/feeds/list/" + spreadsheetID + "/od6/public/values?alt=json";

var photo;
var textBlock;

var leftSide;
var rightSide;
var upperCenter;
var rightTop;

/*
    This function must exist, and must have this name
*/
function prepareNovel()
{
    novel.imagePath = "images/"; // path to your image directory
    novel.audioPath = ""; // path to your audio directory
    
    // initialize your characters, positions, and text blocks here
    n = new Character("");
    
    leftSide = new Position(0, .75, 0, 1);
    rightSide = new Position(800, 450, 1, 1);
    upperCenter = new Position(0.5, 0.3, 0.5, 0.5);
    rightTop = new Position(1, 0.1, 1, 0);
    
    photo = new Character("");  
    lionText = new TextBlock("myText");
    
    // and put your script commands into this array
    script = [
        label, "start",
        scene, "wheat.png",
        n, "Bem vindo à pesquisa interativa da Fatec!",
        n, "Aqui, você vai aprender sobe suas próprias competências, por meio de um simples joguinho de perguntas e respostas!",
        n, "Primeiro, precisamos saber quem você é.",
		
		inputArea, "",
		
		n, "Ótimo! Então, podemos começar para valer!",
		n, "Aqui vai a primeira pergunta!",
		
        label, "questions",

		
    ];
}

