<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.6.2">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="COM-09032">
<packages>
<package name="XDCR_COM-09032">
<wire x1="5.45" y1="14.3" x2="-5.45" y2="14.3" width="0.127" layer="51"/>
<wire x1="4.85" y1="-11.1" x2="-4.85" y2="-11.1" width="0.127" layer="51"/>
<wire x1="4.85" y1="-11.1" x2="4.85" y2="-7.9" width="0.127" layer="51"/>
<wire x1="-4.85" y1="-11.1" x2="-4.85" y2="-7.9" width="0.127" layer="51"/>
<wire x1="4.85" y1="-7.9" x2="7.95" y2="-7.9" width="0.127" layer="51"/>
<wire x1="-4.85" y1="-7.9" x2="-7.95" y2="-7.9" width="0.127" layer="51"/>
<wire x1="9.5" y1="4.1" x2="9.5" y2="-4" width="0.127" layer="51"/>
<wire x1="7.95" y1="4.1" x2="7.95" y2="8" width="0.127" layer="51"/>
<wire x1="7.95" y1="-4" x2="7.95" y2="-7.9" width="0.127" layer="51"/>
<wire x1="7.95" y1="4.1" x2="9.5" y2="4.1" width="0.127" layer="51"/>
<wire x1="7.95" y1="-4" x2="9.5" y2="-4" width="0.127" layer="51"/>
<wire x1="7.95" y1="8" x2="5.45" y2="8" width="0.127" layer="51"/>
<wire x1="-5.45" y1="8" x2="-7.95" y2="8" width="0.127" layer="51"/>
<wire x1="5.45" y1="14.3" x2="5.45" y2="8" width="0.127" layer="51"/>
<wire x1="-5.45" y1="14.3" x2="-5.45" y2="8" width="0.127" layer="51"/>
<wire x1="-7.95" y1="4.9" x2="-11.1" y2="4.9" width="0.127" layer="51"/>
<wire x1="-7.95" y1="-4.9" x2="-11.1" y2="-4.9" width="0.127" layer="51"/>
<wire x1="-11.1" y1="4.9" x2="-11.1" y2="-4.9" width="0.127" layer="51"/>
<wire x1="-7.95" y1="4.9" x2="-7.95" y2="8" width="0.127" layer="51"/>
<wire x1="-7.95" y1="-4.9" x2="-7.95" y2="-7.9" width="0.127" layer="51"/>
<wire x1="-5.45" y1="12.15" x2="5.45" y2="12.15" width="0.127" layer="51" curve="311.462"/>
<wire x1="-6.07" y1="8" x2="-5.45" y2="8" width="0.127" layer="21"/>
<wire x1="-5.45" y1="8" x2="-5.45" y2="14.3" width="0.127" layer="21"/>
<wire x1="-5.45" y1="14.3" x2="5.45" y2="14.3" width="0.127" layer="21"/>
<wire x1="5.45" y1="14.3" x2="5.45" y2="8" width="0.127" layer="21"/>
<wire x1="5.45" y1="8" x2="6.08" y2="8" width="0.127" layer="21"/>
<wire x1="7.95" y1="4.1" x2="9.5" y2="4.1" width="0.127" layer="21"/>
<wire x1="9.5" y1="4.1" x2="9.5" y2="-4" width="0.127" layer="21"/>
<wire x1="9.5" y1="-4" x2="7.95" y2="-4" width="0.127" layer="21"/>
<wire x1="7.95" y1="-4" x2="7.95" y2="-5.12" width="0.127" layer="21"/>
<wire x1="6.08" y1="-7.9" x2="4.85" y2="-7.9" width="0.127" layer="21"/>
<wire x1="4.85" y1="-7.9" x2="4.85" y2="-11.1" width="0.127" layer="21"/>
<wire x1="-4.85" y1="-11.1" x2="-4.85" y2="-7.9" width="0.127" layer="21"/>
<wire x1="-4.85" y1="-7.9" x2="-6.07" y2="-7.9" width="0.127" layer="21"/>
<wire x1="-7.95" y1="-5.17" x2="-7.95" y2="-4.9" width="0.127" layer="21"/>
<wire x1="-7.95" y1="-4.9" x2="-11.1" y2="-4.9" width="0.127" layer="21"/>
<wire x1="-11.1" y1="-4.9" x2="-11.1" y2="4.9" width="0.127" layer="21"/>
<wire x1="-11.1" y1="4.9" x2="-7.95" y2="4.9" width="0.127" layer="21"/>
<wire x1="-5.8" y1="12.35" x2="-5.8" y2="14.6" width="0.05" layer="39"/>
<wire x1="-5.8" y1="14.6" x2="5.7" y2="14.6" width="0.05" layer="39"/>
<wire x1="5.7" y1="14.6" x2="5.7" y2="12.35" width="0.05" layer="39"/>
<wire x1="5.7" y1="12.35" x2="-5.8" y2="12.35" width="0.05" layer="39" curve="-309.72"/>
<circle x="-6.05" y="13.35" radius="0.1" width="0.2" layer="51"/>
<circle x="-6.05" y="13.35" radius="0.1" width="0.2" layer="21"/>
<text x="-5.8" y="14.6" size="1.27" layer="25">&gt;NAME</text>
<text x="-5.8" y="-14.9" size="1.27" layer="27">&gt;VALUE</text>
<pad name="B1A" x="-3.175" y="12.7" drill="0.9" diameter="1.778"/>
<pad name="B1B" x="3.175" y="12.7" drill="0.9" diameter="1.778"/>
<pad name="B2A" x="-3.175" y="7.62" drill="0.9" diameter="1.778"/>
<pad name="B2B" x="3.175" y="7.62" drill="0.9" diameter="1.778"/>
<pad name="H1" x="-2.54" y="-10.16" drill="0.889" diameter="1.778"/>
<pad name="H2" x="0" y="-10.16" drill="0.889" diameter="1.778"/>
<pad name="H3" x="2.54" y="-10.16" drill="0.889" diameter="1.778"/>
<pad name="S1" x="-7.62" y="6.6675" drill="1.397" diameter="2.286"/>
<pad name="S2" x="-7.62" y="-6.6675" drill="1.397" diameter="2.286"/>
<pad name="S3" x="7.62" y="-6.6675" drill="1.397" diameter="2.286"/>
<pad name="S4" x="7.62" y="6.6675" drill="1.397" diameter="2.286"/>
<pad name="V1" x="-10.16" y="2.54" drill="0.889" diameter="1.778"/>
<pad name="V2" x="-10.16" y="0" drill="0.889" diameter="1.778"/>
<pad name="V3" x="-10.16" y="-2.54" drill="0.889" diameter="1.778"/>
</package>
</packages>
<symbols>
<symbol name="COM-09032">
<wire x1="7.62" y1="15.24" x2="7.62" y2="-17.78" width="0.254" layer="94"/>
<wire x1="7.62" y1="-17.78" x2="-7.62" y2="-17.78" width="0.254" layer="94"/>
<wire x1="-7.62" y1="-17.78" x2="-7.62" y2="15.24" width="0.254" layer="94"/>
<wire x1="-7.62" y1="15.24" x2="7.62" y2="15.24" width="0.254" layer="94"/>
<text x="-7.62" y="16.002" size="1.778" layer="95">&gt;NAME</text>
<text x="-7.62" y="-20.32" size="1.778" layer="96">&gt;VALUE</text>
<pin name="V" x="-12.7" y="12.7" length="middle" direction="pas"/>
<pin name="SEL+" x="-12.7" y="-7.62" length="middle" direction="pas"/>
<pin name="H+" x="-12.7" y="0" length="middle" direction="pas"/>
<pin name="H" x="-12.7" y="2.54" length="middle" direction="pas"/>
<pin name="H-" x="-12.7" y="-2.54" length="middle" direction="pas"/>
<pin name="V+" x="-12.7" y="10.16" length="middle" direction="pas"/>
<pin name="V-" x="-12.7" y="7.62" length="middle" direction="pas"/>
<pin name="SEL-" x="-12.7" y="-10.16" length="middle" direction="pas"/>
<pin name="SHIELD" x="-12.7" y="-15.24" length="middle" direction="pas"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="COM-09032" prefix="U">
<description>Thumb Joystick &lt;a href="https://pricing.snapeda.com/parts/COM-09032/SparkFun%20Electronics/view-part?ref=eda"&gt;Check availability&lt;/a&gt;</description>
<gates>
<gate name="G$1" symbol="COM-09032" x="0" y="0"/>
</gates>
<devices>
<device name="" package="XDCR_COM-09032">
<connects>
<connect gate="G$1" pin="H" pad="H2"/>
<connect gate="G$1" pin="H+" pad="H1"/>
<connect gate="G$1" pin="H-" pad="H3"/>
<connect gate="G$1" pin="SEL+" pad="B1A"/>
<connect gate="G$1" pin="SEL-" pad="B2A"/>
<connect gate="G$1" pin="SHIELD" pad="S1 S2 S3 S4"/>
<connect gate="G$1" pin="V" pad="V2"/>
<connect gate="G$1" pin="V+" pad="V1"/>
<connect gate="G$1" pin="V-" pad="V3"/>
</connects>
<technologies>
<technology name="">
<attribute name="AVAILABILITY" value="In Stock"/>
<attribute name="DESCRIPTION" value=" Joystick, 2 - Axis Analog (Resistive) Output "/>
<attribute name="MF" value="SparkFun Electronics"/>
<attribute name="MP" value="COM-09032"/>
<attribute name="PACKAGE" value=" SparkFun Electronics"/>
<attribute name="PRICE" value="None"/>
<attribute name="PURCHASE-URL" value="https://pricing.snapeda.com/search/part/COM-09032/?ref=eda"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="P">
<description>Upverter Parts Library

Created by Upverter.com</description>
<packages>
<package name="MICROCHIP_MCP3008-I-P_0">
<description>CON-ADC-MCP3008-16</description>
<wire x1="-0.635" y1="9.85" x2="0.635" y2="9.85" width="0.2" layer="21" curve="180"/>
<wire x1="-2.65" y1="-9.85" x2="2.65" y2="-9.85" width="0.15" layer="21"/>
<wire x1="0.635" y1="9.85" x2="2.65" y2="9.85" width="0.15" layer="21"/>
<wire x1="-2.65" y1="9.85" x2="-0.635" y2="9.85" width="0.15" layer="21"/>
<wire x1="2.65" y1="-9.85" x2="2.65" y2="9.85" width="0.15" layer="21"/>
<wire x1="-2.65" y1="-9.85" x2="-2.65" y2="9.85" width="0.15" layer="21"/>
<wire x1="-3.55" y1="-9.85" x2="3.55" y2="-9.85" width="0.1" layer="51"/>
<wire x1="-3.55" y1="9.85" x2="3.55" y2="9.85" width="0.1" layer="51"/>
<wire x1="3.55" y1="-9.85" x2="3.55" y2="9.85" width="0.1" layer="51"/>
<wire x1="-3.55" y1="-9.85" x2="-3.55" y2="9.85" width="0.1" layer="51"/>
<wire x1="-4.56" y1="-9.85" x2="-4.56" y2="10.315" width="0.1" layer="39"/>
<wire x1="-4.56" y1="10.315" x2="4.56" y2="10.315" width="0.1" layer="39"/>
<wire x1="4.56" y1="10.315" x2="4.56" y2="-9.85" width="0.1" layer="39"/>
<wire x1="4.56" y1="-9.85" x2="-4.56" y2="-9.85" width="0.1" layer="39"/>
<text x="-5.56" y="10.315" size="1" layer="25">&gt;NAME</text>
<circle x="-1.65" y="8.85" radius="0.3" width="0.6" layer="21"/>
<circle x="-3.81" y="10.19" radius="0.125" width="0.25" layer="21"/>
<circle x="-2.4" y="9" radius="0.5" width="0.1" layer="51"/>
<pad name="9" x="3.81" y="-8.89" drill="0.9" diameter="1.5"/>
<pad name="10" x="3.81" y="-6.35" drill="0.9" diameter="1.5"/>
<pad name="11" x="3.81" y="-3.81" drill="0.9" diameter="1.5"/>
<pad name="12" x="3.81" y="-1.27" drill="0.9" diameter="1.5"/>
<pad name="13" x="3.81" y="1.27" drill="0.9" diameter="1.5"/>
<pad name="14" x="3.81" y="3.81" drill="0.9" diameter="1.5"/>
<pad name="15" x="3.81" y="6.35" drill="0.9" diameter="1.5"/>
<pad name="16" x="3.81" y="8.89" drill="0.9" diameter="1.5"/>
<pad name="8" x="-3.81" y="-8.89" drill="0.9" diameter="1.5"/>
<pad name="7" x="-3.81" y="-6.35" drill="0.9" diameter="1.5"/>
<pad name="6" x="-3.81" y="-3.81" drill="0.9" diameter="1.5"/>
<pad name="5" x="-3.81" y="-1.27" drill="0.9" diameter="1.5"/>
<pad name="4" x="-3.81" y="1.27" drill="0.9" diameter="1.5"/>
<pad name="3" x="-3.81" y="3.81" drill="0.9" diameter="1.5"/>
<pad name="2" x="-3.81" y="6.35" drill="0.9" diameter="1.5"/>
<pad name="1" x="-3.81" y="8.89" drill="0.9" diameter="1.5" shape="square"/>
</package>
</packages>
<symbols>
<symbol name="MICROCHIP_MCP3008-I-P_0_0">
<description>CON-ADC-MCP3008-16</description>
<wire x1="0" y1="-50.8" x2="0" y2="-5.08" width="0.508" layer="94"/>
<wire x1="0" y1="-5.08" x2="17.78" y2="-5.08" width="0.508" layer="94"/>
<wire x1="17.78" y1="-5.08" x2="17.78" y2="-50.8" width="0.508" layer="94"/>
<wire x1="17.78" y1="-50.8" x2="0" y2="-50.8" width="0.508" layer="94"/>
<wire x1="0" y1="-17.78" x2="0" y2="-17.78" width="0.15" layer="94"/>
<wire x1="0" y1="-20.32" x2="0" y2="-20.32" width="0.15" layer="94"/>
<wire x1="17.78" y1="-43.18" x2="17.78" y2="-43.18" width="0.15" layer="94"/>
<wire x1="0" y1="-35.56" x2="0" y2="-35.56" width="0.15" layer="94"/>
<wire x1="0" y1="-38.1" x2="0" y2="-38.1" width="0.15" layer="94"/>
<wire x1="0" y1="-43.18" x2="0" y2="-43.18" width="0.15" layer="94"/>
<wire x1="0" y1="-7.62" x2="0" y2="-7.62" width="0.15" layer="94"/>
<wire x1="0" y1="-12.7" x2="0" y2="-12.7" width="0.15" layer="94"/>
<wire x1="0" y1="-15.24" x2="0" y2="-15.24" width="0.15" layer="94"/>
<wire x1="17.78" y1="-7.62" x2="17.78" y2="-7.62" width="0.15" layer="94"/>
<wire x1="17.78" y1="-48.26" x2="17.78" y2="-48.26" width="0.15" layer="94"/>
<wire x1="0" y1="-48.26" x2="0" y2="-48.26" width="0.15" layer="94"/>
<wire x1="0" y1="-27.94" x2="0" y2="-27.94" width="0.15" layer="94"/>
<wire x1="0" y1="-30.48" x2="0" y2="-30.48" width="0.15" layer="94"/>
<wire x1="0" y1="-22.86" x2="0" y2="-22.86" width="0.15" layer="94"/>
<wire x1="0" y1="-25.4" x2="0" y2="-25.4" width="0.15" layer="94"/>
<text x="0" y="-2.54" size="2.54" layer="95" align="top-left">&gt;NAME</text>
<text x="0" y="-55.88" size="2.54" layer="95" align="top-left">MCP3008-I/P</text>
<pin name="CH2" x="-5.08" y="-17.78" length="middle" direction="in"/>
<pin name="CH3" x="-5.08" y="-20.32" length="middle" direction="in"/>
<pin name="DGND" x="22.86" y="-43.18" length="middle" direction="pwr" rot="R180"/>
<pin name="!CS!/SHDN" x="-5.08" y="-35.56" length="middle" direction="in"/>
<pin name="CLK" x="-5.08" y="-38.1" length="middle" direction="in"/>
<pin name="VREF" x="-5.08" y="-43.18" length="middle" direction="in"/>
<pin name="DIN" x="-5.08" y="-7.62" length="middle" direction="in"/>
<pin name="CH0" x="-5.08" y="-12.7" length="middle" direction="in"/>
<pin name="CH1" x="-5.08" y="-15.24" length="middle" direction="in"/>
<pin name="DOUT" x="22.86" y="-7.62" length="middle" direction="hiz" rot="R180"/>
<pin name="AGND" x="22.86" y="-48.26" length="middle" direction="pwr" rot="R180"/>
<pin name="VDD" x="-5.08" y="-48.26" length="middle" direction="pwr"/>
<pin name="CH6" x="-5.08" y="-27.94" length="middle" direction="in"/>
<pin name="CH7" x="-5.08" y="-30.48" length="middle" direction="in"/>
<pin name="CH4" x="-5.08" y="-22.86" length="middle" direction="in"/>
<pin name="CH5" x="-5.08" y="-25.4" length="middle" direction="in"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="MICROCHIP_MCP3008-I-P" prefix="U">
<description>CON-ADC-MCP3008-16</description>
<gates>
<gate name="G$0" symbol="MICROCHIP_MCP3008-I-P_0_0" x="0" y="0"/>
</gates>
<devices>
<device name="MICROCHIP_MCP3008-I-P_0_0" package="MICROCHIP_MCP3008-I-P_0">
<connects>
<connect gate="G$0" pin="!CS!/SHDN" pad="10"/>
<connect gate="G$0" pin="AGND" pad="14"/>
<connect gate="G$0" pin="CH0" pad="1"/>
<connect gate="G$0" pin="CH1" pad="2"/>
<connect gate="G$0" pin="CH2" pad="3"/>
<connect gate="G$0" pin="CH3" pad="4"/>
<connect gate="G$0" pin="CH4" pad="5"/>
<connect gate="G$0" pin="CH5" pad="6"/>
<connect gate="G$0" pin="CH6" pad="7"/>
<connect gate="G$0" pin="CH7" pad="8"/>
<connect gate="G$0" pin="CLK" pad="13"/>
<connect gate="G$0" pin="DGND" pad="9"/>
<connect gate="G$0" pin="DIN" pad="11"/>
<connect gate="G$0" pin="DOUT" pad="12"/>
<connect gate="G$0" pin="VDD" pad="16"/>
<connect gate="G$0" pin="VREF" pad="15"/>
</connects>
<technologies>
<technology name="">
<attribute name="CIIVA_IDS" value="1029167"/>
<attribute name="CODE__JEDEC" value="MS-001-BB"/>
<attribute name="COMPONENT_LINK_1_DESCRIPTION" value="Manufacturer URL"/>
<attribute name="COMPONENT_LINK_1_URL" value="http://www.microchip.com/"/>
<attribute name="COMPONENT_LINK_3_DESCRIPTION" value="Package Specification"/>
<attribute name="COMPONENT_LINK_3_URL" value="http://www.microchip.com/stellent/groups/techpub_sg/documents/packagingspec/en012702.pdf"/>
<attribute name="DATASHEET" value="http://ww1.microchip.com/downloads/en/DeviceDoc/21295d.pdf"/>
<attribute name="DATASHEET_VERSION" value="revD, Dec-2008"/>
<attribute name="FOOTPRINT_VARIANT_NAME_0" value="Manufacturer Recommended"/>
<attribute name="IMPORTED" value="yes"/>
<attribute name="IMPORTED_FROM" value="vault"/>
<attribute name="IMPORT_TS" value="1521858609"/>
<attribute name="MF" value="Microchip"/>
<attribute name="MPN" value="MCP3008-I/P"/>
<attribute name="PACKAGE" value="PDIP300-P16"/>
<attribute name="PACKAGE_DESCRIPTION" value="16-Lead Plastic Dual In-Line (P) - 300 mil Body [PDIP]"/>
<attribute name="PACKAGE_VERSION" value="revBB, Aug-2009"/>
<attribute name="PIN_0_0_4_INSIDE_EDGE" value="clock"/>
<attribute name="PREFIX" value="U"/>
<attribute name="RELEASE_DATE" value="1331947901"/>
<attribute name="VAULT_GUID" value="2915DD49-D9E5-42B8-8D13-7AC3BE91A6A7"/>
<attribute name="VAULT_REVISION" value="766F0992-63B6-4F6C-8EA7-A406CB97F150"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="U1" library="COM-09032" deviceset="COM-09032" device=""/>
<part name="U2" library="P" deviceset="MICROCHIP_MCP3008-I-P" device="MICROCHIP_MCP3008-I-P_0_0"/>
<part name="U3" library="COM-09032" deviceset="COM-09032" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="U1" gate="G$1" x="50.8" y="30.48" smashed="yes">
<attribute name="NAME" x="43.18" y="46.482" size="1.778" layer="95"/>
<attribute name="VALUE" x="43.18" y="10.16" size="1.778" layer="96"/>
</instance>
<instance part="U2" gate="G$0" x="119.38" y="58.42" smashed="yes">
<attribute name="NAME" x="119.38" y="55.88" size="2.54" layer="95" align="top-left"/>
</instance>
<instance part="U3" gate="G$1" x="50.8" y="81.28" smashed="yes">
<attribute name="NAME" x="43.18" y="97.282" size="1.778" layer="95"/>
<attribute name="VALUE" x="43.18" y="60.96" size="1.778" layer="96"/>
</instance>
</instances>
<busses>
</busses>
<nets>
<net name="VCC_3V3" class="0">
<segment>
<wire x1="50.8" y1="124.46" x2="60.96" y2="124.46" width="0.1524" layer="91"/>
<label x="50.8" y="124.46" size="1.778" layer="95"/>
<label x="101.6" y="15.24" size="1.778" layer="95"/>
<label x="101.6" y="10.16" size="1.778" layer="95"/>
</segment>
</net>
<net name="VCC_5V0" class="0">
<segment>
<wire x1="50.8" y1="119.38" x2="60.96" y2="119.38" width="0.1524" layer="91"/>
<label x="50.8" y="119.38" size="1.778" layer="95"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<wire x1="50.8" y1="114.3" x2="60.96" y2="114.3" width="0.1524" layer="91"/>
<label x="50.8" y="114.3" size="1.778" layer="95"/>
<label x="142.24" y="15.24" size="1.778" layer="95"/>
<label x="142.24" y="10.16" size="1.778" layer="95"/>
</segment>
</net>
<net name="N$1" class="0">
<segment>
<pinref part="U2" gate="G$0" pin="VREF"/>
<wire x1="101.6" y1="15.24" x2="114.3" y2="15.24" width="0.1524" layer="91"/>
</segment>
<segment>
<wire x1="101.6" y1="10.16" x2="114.3" y2="10.16" width="0.1524" layer="91"/>
<pinref part="U2" gate="G$0" pin="VDD"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
