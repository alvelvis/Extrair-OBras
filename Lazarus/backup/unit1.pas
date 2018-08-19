unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls, unix, lclintf;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    ComboBox1: TComboBox;
    procedure Button1Click(Sender: TObject);
    procedure FormShow(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.FormShow(Sender: TObject);
begin
  if not FileExists('titulos_obras.txt') then
  begin
    {$IFDEF LINUX}fpsystem('python obrasprog.py'){$ENDIF}
    {$IFDEF WINDOWS}ExecuteProcess('cmd','/k python obrasprog.py',[]){$ENDIF}
  end;
  ComboBox1.Items.LoadFromFile('titulos_obras.txt');
end;

procedure TForm1.Button1Click(Sender: TObject);
var
  Texto: TStringList;
begin
  Texto := TStringList.Create();
  if FileExists(ComboBox1.Text+'.vislcg3') then OpenDocument(ComboBox1.Text+'.vislcg3')
  else
  begin
    Texto.LoadFromFile('extrair_obra.py');
    Texto.Strings[17] := '	obra = "' + ComboBox1.Text + '"';
    Texto.SaveToFile('extrair_obra.py');
    {$IFDEF LINUX}fpsystem('python extrair_obra.py');{$ENDIF}
    {$IFDEF WINDOWS}ExecuteProcess('cmd','/k python extrair_obra.py',[]);{$ENDIF}
    OpenDocument(ComboBox1.Text+'.vislcg3');
    Texto.Free;
  end;
end;

end.

