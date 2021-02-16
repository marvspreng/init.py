#set knobdefaults

# RotoPaint > Set default tool to brush, set default lifetime for brush and clone to "all frames"  
nuke.knobDefault("RotoPaint.toolbox", "brush {{brush ltt 0} {clone ltt 0}}")
nuke.knobDefault("RotoPaint.toolbox", '''clone {
{ brush opc 0.2}
{ clone opc 0.2}
}''')
nuke.knobDefault("RotoPaint.feather_type", "smooth")
nuke.knobDefault("Roto.feather_type", "smooth") 
nuke.knobDefault("Bezier.output","alpha")
nuke.knobDefault("Bezier.linear","on")

#Misc
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')
nuke.knobDefault( "Grade.black_clamp" , "false" ) 
nuke.knobDefault('STMap.uv', 'rgba')
nuke.knobDefault("EXPTool.mode", "0")
nuke.knobDefault("StickyNote.note_font_size", "50")
nuke.knobDefault('Tracker.label', '[value transform] / ref:[value reference_frame]')
nuke.knobDefault('Switch.label', '[value which]')
nuke.knobDefault('Dissolve.label', '[value which]')
nuke.knobDefault("Blur.label","[value size]")
nuke.knobDefault("Project3D.crop", "0")
nuke.knobDefault("ScanlineRender.motion_vectors_type", "off")
nuke.knobDefault("ScanlineRender.MB_channel", "none")
nuke.knobDefault("TimeOffset.label", "[value time_offset]")
nuke.knobDefault("LensDistortion.gridType", "Thin Line")

# NO CLIPS
nuke.knobDefault("Roto.cliptype","no clip")
nuke.knobDefault("RotoPaint.cliptype","no clip")
nuke.knobDefault("Grid.cliptype","no clip")
nuke.knobDefault("Noise.cliptype","no clip")
nuke.knobDefault("Radial.cliptype","no clip")
nuke.knobDefault("Rectangle.cliptype","no clip")
nuke.knobDefault("Ramp.cliptype","no clip")
nuke.knobDefault("Text2.cliptype","no clip")

#Viewer
nuke.knobDefault("Viewer.freezeGuiWhenPlayBack", "1")  

#bbox
nuke.knobDefault("Merge.bbox", "3")
