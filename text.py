from simulator import PolychromaticField, cf, mm

F = PolychromaticField(
    spectrum=1.5 * cf.illuminant_d65,
    extent_x=15 * mm,
    extent_y=15 * mm,
    Nx=1200,
    Ny=1200,
)

F.add_aperture_from_image(
    "./apertures/text.jpg", pad=(5 * mm, 5 * mm), Nx=1400, Ny=1400
)
rgb = F.compute_colors_at(z=1.5)
F.plot(rgb, xlim=[-10, 10], ylim=[-10, 10])
