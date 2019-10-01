SC040::Del
SC15C::PrintScreen
^SC044::Volume_Mute
^SC057::Volume_Down
^SC058::Volume_Up
^SC041::Media_Prev
^SC042::Media_Play_Pause
^SC043::Media_Next
^SC027::
{
  Send, ''{Left 1}
  Return
}
^+SC027::
{
  ; Enters ``
  Send, {U+0060}{U+0060}{Left 1}
  Return
}
^SC028::
{
  Send, ""{Left 1}
  Return
}
^SC02B::
{
  ; Enters “”
  Send, {U+201C}{U+201D}{Left 1}
  Return
}
